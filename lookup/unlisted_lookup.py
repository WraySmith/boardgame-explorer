"""
mechanics, category, and family are not accessable directly in the api
so they will be gotten indirectly by querying boardgames
"""

import time
import json
import requests

import pandas as pd
import xml.etree.ElementTree as ET


def extract_ids_from_column(column):
    """
    ids in the column exist as ints or lists of ints

    column: pandas series

    returns: flat list of ints
    """

    st = column.astype("str", copy=False).dropna(
        inplace=False
    )  # some columns were mixed type

    strings = st.map(lambda x: x.split(","))
    id_list = set(strings.explode().values)
    return list(id_list)


def make_list_and_explode(input_df, column_name):
    """
    columns are given as strings, need to split into lists

    input_df : dataframe
    column_name : string

    returns : list
    """
    df = input_df.copy(deep=True)
    df[column_name] = (
        df[column_name].astype("str", copy=False).dropna(inplace=False)
    )  # some columns were mixed type

    df[column_name] = df[column_name].map(lambda x: x.split(","))

    df_exp = df.explode(column_name)
    df = df_exp.drop_duplicates(column_name).reset_index()

    return list(set(df["bgg_id"].values))


def create_chunks(id_list, n):
    """
    breaks list into chunks of length n

    id_list : list of ints that are strings
    n : int

    returns : generator of lists
    """

    for i in range(0, len(id_list), n):
        yield id_list[i : i + n]


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


def parse_boardgame_id(id_list, group_type):
    id_name_dict = {}
    id_string = [str(x) for x in id_list]
    id_string = ",".join(id_string)
    url = "https://www.boardgamegeek.com/xmlapi/boardgame"
    url += "/{}".format(id_string)
    print(url)
    resp = requests.get(url)
    tree = ET.fromstring(resp.content)

    for idx, val in enumerate(list(tree)):

        value = val.findall("boardgame{}".format(group_type))
        ids = [x.items()[0][1] for x in value]
        value = [x.text for x in value]

        id_to_name = dict(zip(ids, value))
        id_name_dict.update(id_to_name)
    return id_name_dict


if __name__ == "__main__":

    # one of category, mechanic, or family
    type_of_ids = "mechanic"

    # get list of missing thing
    path_to_save = "./{}_lookup".format(type_of_ids)

    df = pd.read_csv("../data/bgg_GameItem.csv")
    df = df[["bgg_id", type_of_ids]]

    # ids = extract_ids_from_column(df[type_of_ids])

    ids = make_list_and_explode(df, type_of_ids)

    ids_and_names = dict()
    try:
        with open(path_to_save) as f:
            ids_and_names.update(json.load(f))
    except FileNotFoundError:
        pass

    # remove ids that we have already
    print(len(ids))
    ids = list(set(ids) - set((ids_and_names.keys())))
    print(len(ids))

    chunked_ids = create_chunks(ids, 100)

    for id_chunk in chunked_ids:
        try:
            id_and_name = parse_boardgame_id(id_chunk, type_of_ids)
            ids_and_names.update(id_and_name)
        except UnboundLocalError as error:
            print(error)
        except ET.ParseError as error:
            print(error)
        time.sleep(10)

    with open(path_to_save, "w") as fp:
        json.dump(ids_and_names, fp)
