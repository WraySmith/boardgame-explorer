"""
takes data from board_games.csv and changes it to a usable format for the app
"""

import pandas as pd


def call_boardgame_data():
    """
    Returns data from board_game.csv formatted for use in functions
    results in listed values for 'category', 'mechanic, 'publisher'

    Parameters
    ----------
    None

    Returns
    -------
    pandas.DataFrame
    """

    # note that the path is relative to the root folder due to deployment
    # files located in root
    boardgame_data = pd.read_csv(
        "data/app_data/board_game.csv", parse_dates=["year_published"], index_col=0
    )

    boardgame_data["year_published"] = pd.to_datetime(
        boardgame_data["year_published"], format="%Y"
    )

    # convert NA values for these features to a value
    values = {"category": "Unknown", "mechanic": "Unknown", "publisher": "Unknown"}
    boardgame_data.fillna(value=values, inplace=True)

    # create lists from strings
    cats_split = ["category", "mechanic", "publisher"]
    boardgame_data[cats_split] = (
        boardgame_data[cats_split].stack().str.split(r",(?![+ ])").unstack()
    )

    return boardgame_data


def call_boardgame_filter(data, cat, mech, pub, n=None):
    """
    Returns board games filtered based on list of values in
    'category', 'mechanic', 'publisher' columns. Provides
    games in descending order and number of games returned
    can be limited to n.

    Parameters
    ----------
    data: pd.DataFrame
        generated from app_wrangling.call_boardgame_data()
    cat: list, list of categories
    mech: list, list of mechanics
    pub: list, list of publishers
    n: int, optional (default=None)
        number of games to be returned

    Returns
    -------
    pandas.DataFrame
    """
    boardgame_data = data.copy(deep=True)  # deep required as contains lists
    # create dictionary based on user input lists
    columns = {"category": cat, "mechanic": mech, "publisher": pub}
    # creates a list of bool series for each column
    columns_bool = [
        call_bool_series_and(boardgame_data, key, columns[key]) for key in columns
    ]

    # remove rows that aren't matched
    boardgame_data = boardgame_data[
        (columns_bool[0] & columns_bool[1] & columns_bool[2])
    ]

    # sorts by average rating and returns top "n" games if applicable
    boardgame_data = boardgame_data.sort_values("average_rating", ascending=False)
    if n:
        boardgame_data = boardgame_data[:n]

    return boardgame_data


def call_bool_series_and(data, col, list_):
    """
    Takes filter entries and creates bool series to filter dataframe on.
    Logic is based on matching all entries.
    However, if no values in the column are True, then all values changed to True.

    Parameters
    ----------
    data: pd.DataFrame
        generated from app_wrangling.call_boardgame_data()
    col: string, column name to apply function to
    list_: list, list of values to check for

    Returns
    -------
    list of class bool
    """
    list_bool = data[col].apply(lambda x: all(item in x for item in list_))

    # if no True values in entire list, switch all values to True
    if list_bool.sum() == 0:
        list_bool = ~list_bool

    return list_bool


def call_bool_series_or(data, col, list_:
    """
    Takes filter entries and creates bool series to filter dataframe on.
    Logic is based on matching one of entries.

    Parameters
    ----------
    data: pd.DataFrame
        generated from app_wrangling.call_boardgame_data()
    col: string, column name to apply function to
    list_: list, list of values to check for

    Returns
    -------
    list of class bool
    """
    list_bool = boardgame_data[col].apply(lambda x: any(item in x for item in list_))

    return list_bool


def call_boardgame_radio(data, col, list_):
    """
    Returns filtered data based on selecting
    'category','mechanic', or 'publisher' column
    and a list of values.

    data: a pandas df generated from app_wrangling.call_boardgame_data()
    col: string
    list_: list

    return: pandas dataframe
    """
    boardgame_data = data.copy(deep=True)

    boardgame_data = boardgame_data[call_bool_series_or(col, list_, boardgame_data)]

    boardgame_data = form_group(col, list_, boardgame_data)

    boardgame_data = boardgame_data[boardgame_data["group"] != ""]

    return boardgame_data


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
    boardgame_data[col] = list_to_string(boardgame_data[col]).str.split(r",(?![+ ])")
    boardgame_data["group"] = boardgame_data[col].apply(
        lambda x: list(set(x).intersection(set(list_)))
    )
    boardgame_data["group"] = [
        ",(?![+ ])".join(map(str, item)) for item in boardgame_data["group"]
    ]

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





def call_boardgame_top(data, col, year_in, year_out):
    """
    Creates pandas dataframe with top 5
    categories based on user rating

    data: a pandas df generated from app_wrangling.call_boardgame_data()
    col: string
    year_in: int
    year_in: int

    returns: pandas dataframe
    """
    # turns year inputs to date time
    year_in = pd.to_datetime(year_in, format="%Y")
    year_out = pd.to_datetime(year_out, format="%Y")

    # call in boardgame dataframe
    boardgame_data = data.copy(deep=True)

    # create a boolean series to filter by start + end year
    year_filter = (boardgame_data["year_published"] >= year_in) & (
        boardgame_data["year_published"] <= year_out
    )
    boardgame_data = boardgame_data[year_filter]

    # split up column into categorical values
    boardgame_data[col] = boardgame_data[col].str.split(r",(?![+ ])")
    board_game_exp = boardgame_data.explode(col)
    # find the average rating for the top 5 categories
    board_game_exp = (
        board_game_exp.groupby(col)["average_rating"]
        .mean()
        .sort_values(ascending=False)[:5]
        .to_frame()
        .reset_index()
    )

    return board_game_exp


def subset_data(data, col="category"):
    """
    Creates list of categories for column

    data: a pandas df generated from app_wrangling.call_boardgame_data()
    col: string

    return: list
    """

    data_copy = data.copy(deep=True)
    exp_series = data_copy[col].str.split(r",(?![+ ])").explode()

    return list(exp_series.unique())


def remove_columns(data):
    """
    removes columns unnecessary for plotting first two graphs on tab1
    hard coded on columns to remove
    """

    reduced_data = data.drop(
        columns=[
            "Unnamed: 0",
            "game_id",
            "image",
            "max_players",
            "max_playtime",
            "min_age",
            "min_players",
            "min_playtime",
            "playing_time",
            "thumbnail",
            "artist",
            "category",
            "compilation",
            "designer",
            "expansion",
            "family",
            "mechanic",
            "publisher",
            "users_rated",
        ]
    )
    return reduced_data
