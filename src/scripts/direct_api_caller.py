"""
finds ids with out names
queries api
then writes to lookup table

this is a column wise operation

only works for artist, publisher, designer
anything that can be accessed with the api directly
"""
import json
import time
import requests
import xml.etree.ElementTree as ET

import pandas as pd
import utils


def group_id_to_name(id_list, group_name):
    """
    asks the api for names to ids then collects into a dict
    for one group at a time

    id_list : list of ids given as ints
    group_name : string (one of [artist, publisher,
                                 designer, game])

    returns : dictionary

    eg:
    group_id_to_name([100, 150], "publisher")
    """
    id_name_dict = {}
    id_string = [str(x) for x in id_list]
    id_string = ",".join(id_string)
    url = "https://www.boardgamegeek.com/xmlapi/boardgame"
    if group_name != "game":
        url = url + group_name
    url += "/{}".format(id_string)
    print(url)
    resp = requests.get(url)
    tree = ET.fromstring(resp.content)
    for idx, val in enumerate(list(tree)):
        name = val.find("name").text
        id = id_list[idx]
        id_name_dict[id] = name
    return id_name_dict


if __name__ == "__main__":

    # one of artist, publisher, designer,
    type_of_ids = "artist"
    path_to_save = "./data/lookups/{}_lookup.json".format(type_of_ids)

    df = pd.read_csv("./data/bgg_GameItem.csv")
    df = df[["bgg_id", type_of_ids]]

    ids = utils.extract_ids_from_column(df[type_of_ids])

    ids_and_names = dict()
    try:
        with open(path_to_save) as f:
            ids_and_names.update(json.load(f))
    except FileNotFoundError:
        pass

    # remove ids that we have already
    ids = list(set(ids) - set((ids_and_names.keys())))

    chunked_list = list(utils.create_chunks(ids, 500))

    for id_chunk in chunked_list:
        try:
            id_and_name = group_id_to_name(id_chunk, type_of_ids)
            ids_and_names.update(id_and_name)
        except UnboundLocalError as error:
            print(error)
        except ET.ParseError as error:
            print(error)
        time.sleep(10)

    with open(path_to_save, "w") as fp:
        json.dump(ids_and_names, fp)
