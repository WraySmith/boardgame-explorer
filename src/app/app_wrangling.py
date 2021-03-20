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


def call_boardgame_filter(data, cat=[None], mech=[None], pub=[None], n=None):
    """
    Returns board games filtered based on list of values in
    'category', 'mechanic', 'publisher' columns. Provides
    games in descending order and number of games returned
    can be limited to n.

    Parameters
    ----------
    data: pd.DataFrame
        generated from app_wrangling.call_boardgame_data()
    cat: list of str, list of categories
    mech: list of str, list of mechanics
    pub: list of str, list of publishers
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
    list_: list of str, list of values to check for

    Returns
    -------
    list of class bool
    """
    list_bool = data[col].apply(lambda x: all(item in x for item in list_))

    # if no True values in entire list, switch all values to True
    if list_bool.sum() == 0:
        list_bool = ~list_bool

    return list_bool


def call_bool_series_or(data, col, list_):
    """
    Takes filter entries and creates bool series to filter dataframe on.
    Logic is based on matching one of entries.

    Parameters
    ----------
    data: pd.DataFrame
        generated from app_wrangling.call_boardgame_data()
    col: string, column name to apply function to
    list_: list of str, list of values to check for

    Returns
    -------
    list of class bool
    """
    list_bool = data[col].apply(lambda x: any(item in x for item in list_))

    return list_bool


def call_boardgame_radio(data, col, list_, year_in=1900, year_out=2200):
    """
    Returns filtered data based on selecting
    'category','mechanic', or 'publisher' column
    and a list of values.

    Parameters
    ----------
    data: pd.DataFrame
        generated from app_wrangling.call_boardgame_data()
    col: string, column to filter on
    list_: list of str, list of values to check for

    Returns
    -------
    pandas.DataFrame
    """
    boardgame_data = data.copy(deep=True)  # deep required as contains lists
    # filters data based on years provided
    boardgame_data = year_filter(boardgame_data, year_in, year_out)
    # subset based on user selection
    boardgame_data = boardgame_data[call_bool_series_or(boardgame_data, col, list_)]
    # call form_group() to add group column
    boardgame_data = form_group(boardgame_data, col, list_)
    # remove all entries that aren't part of a group
    boardgame_data = boardgame_data[boardgame_data["group"] != ""]

    return boardgame_data


def helper_form_group(x, user_list):
    """
    Helper function to check if all values in user list are met.
    Return "All Selected' if all met.
    """
    if all(item in x for item in user_list):
        return ["All Selected"]
    else:
        return x


def form_group(data, col, list_):
    """
    This takes the selected filter and populates a group column
    indicating which selected values a boardgame has.

    Parameters
    ----------
    data: pd.DataFrame
        generated from app_wrangling.call_boardgame_data()
    col: string, column to filter on
    list_: list of str, list of values to check for

    Returns
    -------
    pandas.DataFrame
    """
    # takes column and forms new one with appropriate groups based on matching
    data["group"] = data[col].apply(lambda x: list(set(x).intersection(set(list_))))

    # replaces groups containing all items with 'All Selected'
    if len(list_) > 1:
        data.group = data["group"].apply(lambda x: helper_form_group(x, list_))

    return data


def count_group(data):
    """
    Provides group counts after `call_boardgame_radio()` is used.

    Parameters
    ----------
    data: pd.DataFrame
        generated from app_wrangling.call_boardgame_radio()

    Returns
    -------
    pandas.DataFrame
    """
    df_out = data.copy(deep=True)
    # explode dataframe, group, and count to new df
    df_out = df_out.explode("group")
    df_out = pd.DataFrame(df_out.groupby(["year_published", "group"]).game_id.count())
    # rearrange df
    df_out = df_out.unstack().droplevel(0, axis=1)

    # if 'All Selected' exists add counts to other categories
    if "All Selected" in df_out.columns:
        # create series from 'All Selected'
        all_addition = df_out["All Selected"].fillna(0)
        # add counts from 'All Selected to each group'
        revised_columns = df_out.drop(columns=["All Selected"]).apply(
            lambda x: x + all_addition.values
        )
        # create revised df
        df_out = pd.concat([revised_columns, df_out[["All Selected"]]], axis=1)

    return df_out


def call_boardgame_top(data, col, year_in, year_out):
    """
    Creates dataframe with top 5 values by user rating in either
    'category', 'mechanic', or 'publisher'

    Parameters
    ----------
    data: pd.DataFrame
        generated from app_wrangling.call_boardgame_data()
    col: string, column to filter on
    year_in: int, start of time period (inclusive)
    year_in: int, end of time period (inclusive)

    Returns
    -------
    pandas.DataFrame
    """
    boardgame_data = data.copy(deep=True)
    # filters data based on years provided
    boardgame_data = year_filter(boardgame_data, year_in, year_out)
    # split up column into categorical values
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


def subset_data(data, col):
    """
    Creates list of categories for column used to populate
    dropdown menus

    Parameters
    ----------
    data: pd.DataFrame
        generated from app_wrangling.call_boardgame_data()
    col: string, column generate list for

    Returns
    -------
    list of strings
    """
    boardgame_data = data.copy(deep=True)
    exp_series = boardgame_data[col].explode()
    return list(exp_series.unique())


def remove_columns(data):
    """
    removes columns unnecessary for plotting first two graphs on tab1

    Parameters
    ----------
    data: pd.DataFrame
        generated from app_wrangling.call_boardgame_data()

    Returns
    -------
    pandas.DataFrame
    """
    boardgame_data = data.copy(deep=True)
    keep = ["name", "year_published", "average_rating"]
    if "group" in boardgame_data.columns:
        keep.append("group")

    return boardgame_data[keep]


def call_boardgame_density(data, col, year_in, year_out):
    """
    Creates dataframe populated with all top 5 values by
    user rating in either 'category', 'mechanic', or 'publisher'

    Parameters
    ----------
    data: pd.DataFrame
        generated from app_wrangling.call_boardgame_data()
    col: string, column to filter on
    year_in: int, start of time period (inclusive)
    year_in: int, end of time period (inclusive)

    Returns
    -------
    pandas.DataFrame
    """
    boardgame_data = data.copy(deep=True)
    boardgame_list = call_boardgame_top(data, col, year_in, year_out)[col].to_list()

    boardgame_data = boardgame_data[
        call_bool_series_or(boardgame_data, col, boardgame_list)
    ]
    boardgame_data = form_group(boardgame_data, col, boardgame_list)
    boardgame_data = boardgame_data.explode("group")

    return boardgame_data


def year_filter(data, year_in, year_out):
    """
    Limits pandas data frame by year range

    Parameters
    ----------
    data: pd.DataFrame
    year_in: int, start of time period (inclusive)
    year_in: int, end of time period (inclusive)

    Returns
    -------
    Boolean.Series
    """
    boardgame_data = data
    # turns year inputs to date time
    year_in = pd.to_datetime(year_in, format="%Y")
    year_out = pd.to_datetime(year_out, format="%Y")

    # create a boolean series to filter by start + end year
    year_filter = (boardgame_data["year_published"] >= year_in) & (
        boardgame_data["year_published"] <= year_out
    )
    boardgame_data = boardgame_data[year_filter]

    return boardgame_data
