import pandas as pd
from sklearn.preprocessing import scale
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.manifold import TSNE


def load_data(filename):
    """
    Load dataframe which is in the format required by the app but
    excluding the x, y, z columns. Fills NA values and creates subset
    of columns for TSNE analysis

    filename: path to csv

    return: boardgame_data_raw, raw data from csv read
    return: boardgame_data_sub, subsetted pd.DataFrame
    """
    boardgame_data_raw = pd.read_csv(filename)
    boardgame_data = boardgame_data_raw.copy()
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

    # create subset of data features
    boardgame_data_sub = boardgame_data.copy()
    boardgame_data_sub = boardgame_data_sub[
        [
            "game_id",
            "name",
            "category",
            "compilation",
            "mechanic",
            "average_rating",
            "users_rated",
        ]
    ]

    return boardgame_data_raw, boardgame_data_sub


def clean_data(data):
    """
    Cleans the subsetted dataframe output from `load_csv()`.
    Data is transformed for the TSNE analysis.

    data: pd.Dataframe, `boardgame_data_sub` output from `load_csv()`

    return: onehot_df, pd.DataFrame of category and mechanics data for TSNE
    return: user_df, pd.Dataframe of `average_rating` and `users_rated`
        for input to TSNE
    """
    boardgame_data_sub = data.copy()
    # compilation and expansion have a high number of values
    # and many boardgames don't have values at all
    # just list whether a game is part of a compilation or expanionsion or not
    boardgame_data_sub[["compilation"]] = (
        boardgame_data_sub[["compilation"]].notna().astype(int)
    )

    # convert category and mechanic to one hot encoding and standardize the columns
    # NOTE: not currently using the one-hot encoded expansion or compilation
    # standardizing resulted in a better TSNE result
    binarizer = MultiLabelBinarizer()
    category = pd.DataFrame(
        scale(binarizer.fit_transform(boardgame_data_sub.category)),
        columns=binarizer.classes_,
    )
    binarizer = MultiLabelBinarizer()
    mechanic = pd.DataFrame(
        scale(binarizer.fit_transform(boardgame_data_sub.mechanic)),
        columns=binarizer.classes_,
    )
    onehot_df = pd.concat([category, mechanic], axis=1)
    onehot_df

    # numeric user rating categories
    # it was found that not standardizing creates a better TSNE result for this axis
    user_df = pd.DataFrame(
        scale(boardgame_data_sub[["average_rating", "users_rated"]]),
        columns=["average_rating", "users_rated"],
    )

    return onehot_df, user_df


def tsne_analyse(onehot_df, user_df):
    """
    Runs TSNE analysis and provides output.

    onehot_df: pd.Dataframe, output from `clean_data()`
    user_df: pd.Dataframe, output from `clean_data()`

    return: tsne_cat_df, pd.DataFrame of output from category/mechanic TSNE
    return: tsne_user_df, pd.DataFrame of output from user rating TSNE
    """
    # run TSNE on one-hot encoded category and mechanic features
    # a high perplexity fo 50 was found to provide a good visual result
    tsne_cat = TSNE(perplexity=50, n_components=2)

    tsne_cat_results = tsne_cat.fit_transform(onehot_df)
    # run TSNE on user ratings features
    # this is done as we want a separate axis related to user rating
    tsne_user = TSNE(perplexity=50, n_components=1)
    tsne_user_results = tsne_user.fit_transform(user_df)

    # create a dataframe for output
    tsne_cat_df = pd.DataFrame(tsne_cat_results, columns=["x", "y"])
    # note: dividing user tsne results by 2 and multiply by -1 for plotting purposes
    tsne_user_df = pd.DataFrame((tsne_user_results * -1) / 2, columns=["z"])

    return tsne_cat_df, tsne_user_df


if __name__ == "__main__":
    # load data and create subset for analysis
    filename = "./data/processed/bgg_wrangled.csv"
    raw, mod = load_data(filename)
    print("Data loaded successfully")

    # clean dataframe and create cleaned and transformed datasets for analysis
    cat_mec, user = clean_data(mod)
    print("Data transformed successfully")

    # run TSNE analysis
    result_cat, result_user = tsne_analyse(cat_mec, user)
    print("TSNE analysis complete")

    # save data
    combined_output = pd.concat([raw, result_cat, result_user], axis=1)
    combined_output.to_csv("./data/processed/bgg_data" + "_tsne.csv", index=False)
    print("Dataframe saved")
