"""
compares the old dataset we used for 550
with the new one from bbg with scraped information instead of ids
"""

import pandas as pd

if __name__ == "__main__":

    cols = ["designer", "artist", "family", "publisher"]

    for col in cols:
        new = pd.read_csv("./data/processed/bgg_with_names.csv")
        old = pd.read_csv("./reports/exploratory_data_analysis/board_games_EDA.csv")
        old = old.rename(columns={"game_id": "bgg_id"})

        new = new[["bgg_id", col]]
        old = old[["bgg_id", col]]

        # collect common ids
        ids = set(old["bgg_id"].values).intersection(set(new["bgg_id"].values))

        mask = new["bgg_id"].isin(ids)
        filtered_new = new.loc[mask]

        mask = old["bgg_id"].isin(ids)
        filtered_old = old.loc[mask]

        joined = pd.merge(filtered_new, filtered_old, on="bgg_id")

        # TODO change to check non empty intersect
        joined["is_match"] = joined["{}_x".format(col)] == joined["{}_y".format(col)]
        print("percent match for {} is : {}%".format(col, joined["is_match"].mean()))

        # percent match for designer is : 0.9581709287955129%
        # percent match for artist is : 0.5920714896853313%
        # percent match for family is : 0.08945717273505085%
        # percent match for publisher is : 0.6208765091738758%
