import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("data/raw/" + "bgg_data_from_api.csv")

    # rename columns
    df = df.rename(
        columns={
            "year": "year_published",
            "maxplayers": "max_players",
            "minplayers": "min_players",
            "maxplaytime": "max_playtime",
            "avg_rating": "average_rating",
            "bgg_id": "game_id",
            "num_votes": "users_rated",
            "minplaytime": "min_playtime",
            "age": "min_age",
        }
    )

    df = df.dropna(subset=["year_published"])

    df["year_published"] = df["year_published"].astype("int")

    gt_50 = df[df["users_rated"] > 100]

    between_1950_2021 = gt_50[(gt_50["year_published"] >= 1950)]

    between_1950_2021["year_published"] = between_1950_2021["year_published"].astype(
        "str"
    )

    print(between_1950_2021.shape)

    between_1950_2021.to_csv("data/processed/bgg_wrangled.csv")
