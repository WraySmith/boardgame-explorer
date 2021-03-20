import pandas as pd
from sklearn.preprocessing import scale
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.manifold import TSNE

# load data
def load_data(filename):
    boardgame_data_raw = pd.read_csv("board_game_tsne.csv")
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
            "expansion",
            "mechanic",
            "average_rating",
            "users_rated",
        ]
    ]


# compilation and expansion have a high number of values
# and many boardgames don't have values at all
# just list whether a game is part of a compilation or expanionsion or not
boardgame_data_sub[["expansion", "compilation"]] = (
    boardgame_data_sub[["expansion", "compilation"]].notna().astype(int)
)

# convert category and mechanic to one hot encoding and standardize the columns
# NOTE: note currently using the one-hot encoded expansion or compilation
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
user_scaled = pd.DataFrame(
    scale(boardgame_data_sub[["average_rating", "users_rated"]]),
    columns=["average_rating", "users_rated"],
)

# run TSNE on one-hot encoded category and mechanic features
# a high perplexity fo 50 was found to provide a good visual result
tsne_cat = TSNE(perplexity=50, n_components=2)
tsne_cat_results = tsne_cat.fit_transform(onehot_df)
# run TSNE on user ratings features
# this is done as we want a separate axis related to user rating
tsne_user = TSNE(perplexity=50, n_components=1)
tsne_user_results = tsne_user.fit_transform(user_scaled)

# create a dataframe for output
tsne_cat_df = pd.DataFrame(tsne_cat_results, columns=["x", "y"])
# note: dividing user tsne results by 2 for plotting purposes
tsne_user_df = pd.DataFrame((tsne_user_results * -1) / 2, columns=["z"])
combined_output = pd.concat([boardgame_data_raw, tsne_cat_df, tsne_user_df], axis=1)

# save data
combined_output.to_csv("board_game_tsne_processed.csv", index=False)


"board_game_tsne.csv"