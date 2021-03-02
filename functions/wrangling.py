"""
takes data from board_games.csv and changes it to a usable format
"""

import pandas as pd

"""
Returns data from board_game.csv

return: panda dataframe
"""


def call_boardgame_data(cat, mech, pub):
    """
    Returns data from board_game.csv

    return: panda dataframe
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

    boardgame_data = boardgame_data[bool_generator(cat, mech, pub, boardgame_data)]

    return boardgame_data


def list_to_string(list_):
    """
    This takes in a list and changes its format to a
    string that can be read by .match() function

    input: list

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

    input: string

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
        mech_bool = boardgame_data["mechanics"].str.match(mech)
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
