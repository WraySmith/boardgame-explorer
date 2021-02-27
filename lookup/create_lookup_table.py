"""
finds ids with out names
queries api
then writes to lookup table
"""

import pandas as pd

import id_lookup


def extract_ids_from_column(column):
    """
    ids in the column exist as ints or lists of ints

    column: pandas series

    returns: flat list of ints
    """
    id_list = []

    st = column.astype("str", copy=False).dropna(
        inplace=False
    )  # some columns were mixed type

    for item in list(st):
        temp = item.split(",")
        id_list.extend(temp)
    return list(set(id_list))


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
    df = pd.read_csv("../data/bgg_GameItem.csv")
    df = df[["bgg_id", "publisher"]]

    ids = extract_ids_from_column(df["publisher"])

    chunked_list = list(create_chunks(ids, 500))
    pub_id = id_lookup.group_id_to_name(chunked_list[-1], "publisher")
    print(pub_id)
