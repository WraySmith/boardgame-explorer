"""
makes our new csv look like our old

first run apply_lookups.py
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
    print("applying look up")
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
    print("finished applying look up")
    return df


def wrangle_df(dataframe):
    """
    changes dataframe to desired shape

    dataframe : df

    returns : df
    """

    # only select games with more than 50 reviews
    gt_50_reviews = dataframe[dataframe.num_votes >= 50]

    # filter between 1950 and 2021
    between_1950_2021 = gt_50_reviews[
        (gt_50_reviews["year"] >= 1950) & (gt_50_reviews["year"] <= 2021)
    ]

    # select desired columns
    df_w_proper_columns = between_1950_2021[
        [
            "bgg_id",
            "max_players",
            "max_time",
            "min_age",
            "min_players",
            "min_time",
            "name",
            "year",
            "artist",
            "category",
            "compilation",
            "designer",
            "family",
            "mechanic",
            "publisher",
            "avg_rating",
            "num_votes",
            "rank",
        ]
    ]

    return df_w_proper_columns


if __name__ == "__main__":
    df_to_wrangle = pd.read_csv("../data/raw/bgg_GameItem.csv")
    # df_to_wrangle = pd.read_csv("../data/processed/bgg_with_names.csv")
    wrangled = wrangle_df(df_to_wrangle)

    group_types = ["category", "artist", "designer", "family", "mechanic", "publisher"]

    df_copy = wrangled.copy(deep=True)
    for group_type in group_types:
        df_copy = apply_lookup(df_copy, group_type)

    df_copy.to_csv("../data/processed/bgg_with_names.csv")

# Index(['Unnamed: 0', 'bgg_id', 'name', 'year', 'game_type', 'designer',
#        'artist', 'publisher', 'min_players', 'max_players', 'min_players_rec',
#        'max_players_rec', 'min_players_best', 'max_players_best', 'min_age',
#        'min_age_rec', 'min_time', 'max_time', 'category', 'mechanic',
#        'cooperative', 'compilation', 'compilation_of', 'family',
#        'implementation', 'integration', 'rank', 'num_votes', 'avg_rating',
#        'stddev_rating', 'bayes_rating', 'complexity', 'language_dependency',
#        'bga_id', 'dbpedia_id', 'luding_id', 'spielen_id', 'wikidata_id',
#        'wikipedia_id'],
#       dtype='object')
# Index(['game_id', 'description', 'image', 'max_players', 'max_playtime',
#        'min_age', 'min_players', 'min_playtime', 'name', 'playing_time',
#        'thumbnail', 'year_published', 'artist', 'category', 'compilation',
#        'designer', 'expansion', 'family', 'mechanic', 'publisher',
#        'average_rating', 'users_rated'],
#       dtype='object')
