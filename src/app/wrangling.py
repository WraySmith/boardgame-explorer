"""
takes data from board_games.csv and changes it to a usable format
"""

import pandas as pd


def call_boardgame_data():
    """
    Returns data from board_game.csv

    return: pandas dataframe
    """

    # reads csv
    boardgame_data = pd.read_csv("board_game.csv", parse_dates=["year_published"])
    boardgame_data["year_published"] = pd.to_datetime(
        boardgame_data["year_published"], format="%Y"
    )

    # convert NA values for these features to a value
    values = {"category": "Unknown", "mechanic": "Unknown", "publisher": "Unknown"}
    boardgame_data.fillna(value=values, inplace=True)

    return boardgame_data


def call_boardgame_filter(cat, mech, pub, n):
    """
    Wraps call_boardgame_data
    Returns filtered data based on list of
    values in 'category', 'mechanic', and
    'publisher' columns.

    cat: list
    mech: list
    pub: list
    n: int

    return: pandas dataframe
    """
    boardgame_data = call_boardgame_data()
    # create dictionary based on inputted lists.
    columns = {"category": cat, "mechanic": mech, "publisher": pub}
    # creates a list of bool series for each column
    column_bool = [
        call_bool_series_and(key, columns[key], boardgame_data) for key in columns
    ]
    # checks if no input was provided and returns entirety of data
    if (column_bool[0] | column_bool[1] | column_bool[2]).sum() != 0:
        boardgame_data = boardgame_data[
            (column_bool[0] & column_bool[1] & column_bool[2])
        ]

    # sorts by average rating and returns top "n" games
    if n is not None:
        boardgame_data = boardgame_data.sort_values("average_rating", ascending=False)[
            :n
        ]

    return boardgame_data


def call_boardgame_radio(col, list_):
    """
    Wraps call_boardgame_data
    Returns filtered data based on selecting
    'category','mechanic', or 'publisher' column
    and a list of values.

    col: string
    list_: list

    return: pandas dataframe
    """
    boardgame_data = call_boardgame_data()

    boardgame_data = boardgame_data[call_bool_series_or(col, list_, boardgame_data)]

    boardgame_data = form_group(col, list_, boardgame_data)

    return boardgame_data


def list_to_string(list_):
    """
    This takes in a list and changes its format to a
    string that can be read by .match() function

    list_: list

    returns: string
    """
    if type(list_) is list:
        list_ = str(list_).strip("[']").replace(", ", "").replace("''", "|")
        return list_
    else:
        return list_


def form_group(col, list_, boardgame_data):
    """
    This takes the selected filter and forms
    appropriate groups column.

    col: string
    list_: list
    boardgame_data: pandas dataframe

    returns: pandas dataframe
    """
    # takes column and forms new one with appropriate groups
    boardgame_data[col] = boardgame_data[col].map(lambda x: x.split(","))
    boardgame_data["group"] = boardgame_data[col].apply(
        lambda x: list(set(x).intersection(set(list_)))
    )
    boardgame_data["group"] = [",".join(map(str, l)) for l in boardgame_data["group"]]

    # replaces cross product groups containing all items with generic group
    if len(list_) > 1:
        boardgame_data.loc[
            boardgame_data["group"].apply(lambda x: all(item in x for item in list_)),
            "group",
        ] = "All Selected"
        # removes cross products with not all items
        boardgame_data = boardgame_data[
            ~boardgame_data["group"].apply(lambda x: x not in list_ + ["All Selected"])
        ]

    return boardgame_data


def call_bool_series_or(col, list_, boardgame_data):
    """
    Takes filters entries and creates bool series to filter

    col: string
    list_: list
    boardgame_data: pandas dataframe

    returns: bool series
    """
    list_ = list_to_string(list_)
    list_bool = boardgame_data[col].str.match(list_)

    return list_bool


def call_bool_series_and(col, list_, boardgame_data):
    """
    Takes filters entries and creates bool series to filter

    col: string
    list_: list
    boardgame_data: pandas dataframe

    returns: bool series
    """
    list_bool = boardgame_data[col].apply(lambda x: all(item in x for item in list_))

    if list_bool.sum() == 0:
        list_bool = ~list_bool

    return list_bool


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


def subset_data(col="category"):
    """
    Creates list of categories for column

    col: string

    return: list
    """

    data_copy = call_boardgame_data()
    data_copy[col] = data_copy[col].str.split(",").explode(col)

    return list(data_copy[col].unique())