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
    return set(id_list)


if __name__ == "__main__":
    df = pd.read_csv("../data/bgg_GameItem.csv")
    df = df[["bgg_id", "publisher"]]

    ids = extract_ids_from_column(df["publisher"])
    print(len(ids))
