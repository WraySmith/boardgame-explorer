"""
creates lookup tables for numeric data that should have a corresponding name/string
"""

import requests

import pandas as pd
import bs4


def scrape_game(game_id=15):
    """
    gets soup for given game

    url only needs the game_id, since it will auto complete the name
    """

    url = "https://boardgamegeek.com/boardgame/{}".format(game_id)
    print(url)


if __name__ == "__main__":

    # df = pd.read_csv("bgg_GameItem.csv")

    # print(df.head(20))
    scrape_game(game_id=13)
