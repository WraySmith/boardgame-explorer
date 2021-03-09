"""
mechanics, category, and family are not accessable directly in the api
so they will be gotten indirectly by querying boardgames

this is a row wise operation

works by finding requested information inside a boardgame's api response
"""

import json
import time
import xml.etree.ElementTree as ET

import pandas as pd
import requests
import utils


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

    # currently done maually
    # one of category, mechanic, or family
    type_of_ids = "designer"

    path_to_save = "./data/lookups/{}_lookup.json".format(type_of_ids)

    df = pd.read_csv("./data/raw/bgg_GameItem.csv")
    df = df[["bgg_id", type_of_ids]]

    ids = make_list_and_explode(df, type_of_ids)

    ids_and_names = dict()
    try:
        with open(path_to_save) as f:
            ids_and_names.update(json.load(f))
    except FileNotFoundError:
        pass

    # TODO remove ids we have already as to not scrape redundantly

    chunked_ids = utils.create_chunks(ids, 100)

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
