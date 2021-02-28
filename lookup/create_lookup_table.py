"""
finds ids with out names
queries api
then writes to lookup table
"""
import json
import time

import pandas as pd

import id_lookup


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


if __name__ == "__main__":

    type_of_ids = "publisher"
    path_to_save = "./{}_lookup".format(type_of_ids)

    df = pd.read_csv("../data/bgg_GameItem.csv")
    df = df[["bgg_id", type_of_ids]]

    ids = extract_ids_from_column(df[type_of_ids])
    chunked_list = list(create_chunks(ids, 500))
    ids_and_names = dict()

    for id_chunk in chunked_list:
        id_and_name = id_lookup.group_id_to_name(id_chunk, type_of_ids)
        ids_and_names.update(id_and_name)
        time.sleep(10)

    with open(path_to_save, "w") as fp:
        json.dump(ids_and_names, fp)
