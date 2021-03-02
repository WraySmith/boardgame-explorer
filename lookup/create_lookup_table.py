"""
finds ids with out names
queries api
then writes to lookup table
"""
import json
import time

import pandas as pd

import id_lookup

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


def create_chunks(id_list, n):
    """
    breaks list into chunks of length n

    id_list : list of ints that are strings
    n : int

    returns : generator of lists
    """

    for i in range(0, len(id_list), n):
        yield id_list[i : i + n]


def subtract_old_ids(old_ids, new_ids):
    """
    removes ids from look up list if they have already been saved to the lookup table

    old_ids : dictionary
    new_ids : list

    returns : list
    """

    old_id_list = old_ids.keys()

    return


if __name__ == "__main__":

    # artist, publisher,
    # designer, category, mechanic, game

    type_of_ids = "family"
    path_to_save = "./{}_lookup.json".format(type_of_ids)

    df = pd.read_csv("../data/bgg_GameItem.csv")
    df = df[["bgg_id", type_of_ids]]

    ids = extract_ids_from_column(df[type_of_ids])

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

    chunked_list = list(create_chunks(ids, 500))

    for id_chunk in chunked_list:
        try:
            id_and_name = id_lookup.group_id_to_name(id_chunk, type_of_ids)
            ids_and_names.update(id_and_name)
        except UnboundLocalError as error:
            print(error)
        except ET.ParseError as error:
            print(error)
        time.sleep(10)

    with open(path_to_save, "w") as fp:
        json.dump(ids_and_names, fp)
