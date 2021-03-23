"""
Gets a list of boardgame ids
turns the list into chunks
queries the bgg api with a chunk at a time
to collect named values for the board game dataset
"""

import xml.etree.ElementTree as ET

import pandas as pd
import requests
import utils

import time


def parse_game_ids(game_ids):
    game_ids = ",".join(str(x) for x in game_ids)
    url = url = "https://www.boardgamegeek.com/xmlapi/boardgame/{}?stats=1".format(
        game_ids
    )
    print(url)
    resp = requests.get(url)
    tree = ET.fromstring(resp.content)

    rows = []

    column_names = [
        "bgg_id",
        "maxplayers",
        "maxplaytime",
        "age",
        "minplayers",
        "minplaytime",
        "name",
        "year_published",
        "artist",
        "category",
        "compilation",
        "designer",
        "family",
        "mechanic",
        "publisher",
        "users_rated",
        "average_rating",
    ]

    id_list = []
    for child in tree:
        id_list.append(child.attrib["objectid"])

    for idx, val in enumerate(list(tree)):
        # name
        name = ""
        value = val.findall("name")
        for v in value:
            if "primary" in set(v.attrib.keys()):
                name = v.text
        if not name:
            name = [x.text for x in value][0]

        # maxplayers
        value = val.findall("maxplayers")
        maxplayers = value[0].text

        # max_time
        value = val.findall("maxplaytime")
        maxplaytime = value[0].text

        # min_age
        value = val.findall("age")
        age = value[0].text

        # minplayers
        value = val.findall("minplayers")
        minplayers = value[0].text

        # minplaytime
        value = val.findall("minplaytime")
        minplaytime = value[0].text

        # id
        bgg_id = id_list[idx]

        # year published
        value = val.findall("yearpublished")
        year_published = value[0].text

        # artist
        value = val.findall("boardgameartist")
        artist = [x.text for x in value]

        # category
        value = val.findall("boardgamecategory")
        category = [x.text for x in value]

        # compilation
        value = val.findall("boardgamecompilation")
        compilation = [x.text for x in value]

        # designer
        value = val.findall("boardgamedesigner")
        designer = [x.text for x in value]

        # family
        value = val.findall("boardgamefamily")
        family = [x.text for x in value]

        # mechanic
        value = val.findall("boardgamemechanic")
        mechanic = [x.text for x in value]

        # publisher
        value = val.findall("boardgamepublisher")
        publisher = [x.text for x in value]

        # stats
        stats = val.find("statistics")
        ratings = stats.find("ratings")
        user_ratings = ratings.find("usersrated").text
        average_rating = ratings.find("average").text

        row = [
            bgg_id,
            maxplayers,
            maxplaytime,
            age,
            minplayers,
            minplaytime,
            name,
            year_published,
            artist,
            category,
            compilation,
            designer,
            family,
            mechanic,
            publisher,
            user_ratings,
            average_rating,
        ]
        rows.append(row)
    df = pd.DataFrame(rows, columns=column_names)

    list_columns = [
        "artist",
        "category",
        "compilation",
        "designer",
        "family",
        "mechanic",
        "publisher",
    ]
    for col in list_columns:
        df[col] = [",".join(map(str, x)) for x in df[col]]

    print(df.head())
    print(df.shape)
    print("sleeping")
    time.sleep(10)
    return df


if __name__ == "__main__":
    # new_data = pd.read_csv("./data/raw/bgg_GameItem.csv")
    # game_ids = list(new_data["bgg_id"])
    # chunked_game_ids = utils.create_chunks(game_ids, 500)

    # df_list = []

    # for id_chunk in list(chunked_game_ids):
    #     df_list.append(parse_game_ids(id_chunk))

    # df = pd.concat(df_list)

    # print(df.head())
    # print(df.shape)

    # df.to_csv("./data/processed/bgg_with_scraped_names.csv")

