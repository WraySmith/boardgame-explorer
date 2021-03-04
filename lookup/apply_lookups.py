"""
convert columns with ids to names via scrapped lookup tables
"""

import json

import pandas as pd


def apply_lookup(dataframe, group_type):
    """
    converts df[group_type] from ids to names

    dataframe : df
    group_type : string

    returns : df
    """
    print("working with {}".format(group_type))
    df = dataframe.copy(deep=True)
    df[group_type] = (
        df[group_type].astype("str", copy=False).dropna(inplace=False)
    )  # some columns were mixed type

    # load the lookup table
    path_to_save = "./{}_lookup.json".format(group_type)
    with open(path_to_save) as f:
        lookup = json.load(f)
    lookup["nan"] = "None"

    # explode by group_type
    df[group_type] = df[group_type].map(lambda x: x.split(","))
    df_exp = df.explode(group_type)

    # apply lookup
    df_exp[group_type] = df_exp[group_type].map(lambda x: lookup[x])

    # implode
    df_imp = (
        df_exp[["bgg_id", group_type]]
        .groupby("bgg_id")
        .agg(lambda x: ",".join(x))
        .reset_index()
    )

    # join back
    df[group_type] = df_imp[group_type]

    print("finished with {}".format(group_type))
    # return
    return df


if __name__ == "__main__":

    group_types = ["category", "artist", "designer", "family", "mechanic", "publisher"]

    df = pd.read_csv("../data/bgg_GameItem.csv")

    df_copy = df.copy(deep=True)
    for group_type in group_types:
        df_copy = apply_lookup(df_copy, group_type)

    df_copy.to_csv("../data/bgg_with_names.csv")
