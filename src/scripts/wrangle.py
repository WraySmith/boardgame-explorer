import pandas as pd

if __name__ == "__main__":
    df_with_names = pd.read_csv("data/processed/" + "bgg_with_scraped_names.csv")
    df_with_scores = pd.read_csv("data/raw/" + "bgg_GameItem.csv")
    old_data = pd.read_csv("data/app_data/board_game.csv")

    df_with_scores_subset = df_with_scores[["bgg_id", "num_votes", "avg_rating"]]

    merged = df_with_names.merge(df_with_scores_subset, how="inner", on="bgg_id")

    # rename columns
    merged = merged.rename(
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
    print("new columns")
    print(merged.columns)
    print("old columns")
    print(old_data.columns)

    merged = merged.dropna(subset=["year_published"])

    merged["year_published"] = merged["year_published"].astype("int")

    gt_50 = merged[merged["users_rated"] > 50]

    between_1950_2021 = gt_50[
        (gt_50["year_published"] >= 1950) & (gt_50["year_published"] <= 2021)
    ]

    merged["year_published"] = merged["year_published"].astype("str")

    print(between_1950_2021.shape)

    between_1950_2021.to_csv("data/app_data/new.csv")
