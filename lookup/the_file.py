"""
creates lookup tables for numeric data that
should have a corresponding name/string
"""

import time

# import json
import requests

# import pandas as pd
from bs4 import BeautifulSoup


def get_game_soup(game_id=15):
    """
    gets soup for given game

    url only needs the game_id, since it will auto complete the name
    """
    url = "https://boardgamegeek.com/boardgame/{}".format(game_id)
    resp = requests.get(url)

    time.sleep(1)
    if resp.status_code != 200:
        print("failed because of error: {}".format(resp))
        print("when looking for game with id: {}".format(game_id))
        print("add error handling")
        raise RuntimeError("Failed to scrape site")

    soup = BeautifulSoup(resp.content, "html.parser")
    return soup


def get_soup_for_id_and_group(group, bgg_id):
    """
    collects the name for the given id and group
    """
    possible_groups = set("artist", "publisher", "category", "mechanic", "designer")
    if group not in possible_groups:
        raise RuntimeError("Incorrect group given")

    base_url = "https://boardgamegeek.com/boardgame"
    url = base_url + group + "/" + str(bgg_id)
    print(url)


if __name__ == "__main__":

    # df = pd.read_csv("bgg_GameItem.csv")

    # print(df.head(20))
    soup = get_game_soup(game_id=13)
    script = soup.find_all("script")[1]
    print(str(script))
