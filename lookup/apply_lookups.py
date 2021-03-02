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


if __name__ == "__main__":

    df = pd.read_csv("../data/bgg_GameItem.csv")
    print(df.head())
