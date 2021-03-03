"""
takes data from board_games.csv and changes it to a usable format
"""

import pandas as pd

"""
Returns data from board_game.csv

return: panda dataframe
"""


def call_boardgame_data():
    """
    Returns data from board_game.csv

    return: pandas dataframe
    """

    # reads csv
    boardgame_data = pd.read_csv(
        "../data/board_game.csv", parse_dates=["year_published"]
    )
    boardgame_data["year_published"] = pd.to_datetime(
        boardgame_data["year_published"], format="%Y"
    )

    # convert NA values for these features to a value
    values = {"category": "Unknown", "mechanic": "Unknown", "publisher": "Unknown"}
    boardgame_data.fillna(value=values, inplace=True)

    return boardgame_data


def call_boardgame_filter(cat, mech, pub):
    """
    Returns filtered data from board_game.csv

    cat: list
    mech: list
    pub: list

    return: pandas dataframe
    """
    boardgame_data = call_boardgame_data()

    boardgame_data = boardgame_data[bool_generator(cat, mech, pub, boardgame_data)]

    return boardgame_data


def list_to_string(list_):
    """
    This takes in a list and changes its format to a
    string that can be read by .match() function

    list_: list

    returns: string
    """
    if list_ is list:
        str(list_).strip("[']").replace(", ", "").replace("''", "|")
        return list_
    else:
        return list_


def bool_generator(cat, mech, pub, boardgame_data):
    """
    Takes filters entries and creates bool table to filter

    cat: list
    mech: list
    pub: list
    boardgame_data: pandas dataframe

    returns: bool series
    """
    # This can probably be simplified into a lambda function
    if cat is not None:
        cat = list_to_string(cat)
        cat_bool = boardgame_data["category"].str.match(cat)
    else:
        cat_bool = False

    if mech is not None:
        mech = list_to_string(mech)
        mech_bool = boardgame_data["mechanic"].str.match(mech)
    else:
        mech_bool = False

    if pub is not None:
        pub = list_to_string(pub)
        pub_bool = boardgame_data["publisher"].str.match(pub)
    else:
        pub_bool = False

    if (cat_bool + mech_bool + pub_bool).sum() == 0:
        return ~boardgame_data["game_id"].isna()
    else:
        return cat_bool + mech_bool + pub_bool


def call_boardgame_top(col, year_in, year_out):
    """
    Creates pandas dataframe with top 5
    categories based on user rating

    col: string
    year_in: int
    year_in: int

    returns: pandas dataframe
    """
    # turns year inputs to date time
    year_in = pd.to_datetime(year_in, format="%Y")
    year_out = pd.to_datetime(year_out, format="%Y")

    # call in boardgame dataframe
    boardgame_data = call_boardgame_data()

    # create a boolean series to filter by start + end year
    year_filter = (boardgame_data["year_published"] >= year_in) & (
        boardgame_data["year_published"] <= year_out
    )
    boardgame_data = boardgame_data[year_filter]

    # split up column into categorical values
    boardgame_data[col] = boardgame_data[col].str.split(",").explode(col)
    # find the average rating for the top 5 categories
    boardgame_data = (
        boardgame_data.groupby(col)["average_rating"]
        .mean()
        .sort_values(ascending=False)[:5]
        .to_frame()
        .reset_index()
    )

    return boardgame_data
