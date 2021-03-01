"""
mechanics, category, and family are not accessable directly in the api
so they will be gotten indirectly by querying boardgames
"""

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


if __name__ == "__main__":

    # one of category, mechanic, or family
    type_of_ids = "mechanic"

    # get list of missing thing
    path_to_save = "./{}_lookup".format(type_of_ids)

    df = pd.read_csv("../data/bgg_GameItem.csv")
    df = df[["bgg_id", type_of_ids]]

    # ids = extract_ids_from_column(df[type_of_ids])

    ids = make_list_and_explode(df, type_of_ids)
    chunked_ids = create_chunks(ids, 100)

    for ids in chunked_ids:
        print(len(ids))

