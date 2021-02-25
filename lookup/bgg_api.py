"""
working with the bgg api
"""

import requests
import xml.etree.ElementTree as ET


def get_publisher_id_name_dict(publisher_list):
    id_name_dict = {}
    publishers_string = [str(x) for x in publisher_list]
    publishers_string = ",".join(publishers_string)
    url = "https://www.boardgamegeek.com/xmlapi/boardgamepublisher/{}".format(
        publishers_string
    )
    resp = requests.get(url)
    tree = ET.fromstring(resp.content)
    publishers = list(tree)
    for idx, publisher in enumerate(publishers):
        pub_name = publisher.find("name").text
        pub_id = publisher_list[idx]
        id_name_dict[pub_id] = pub_name
    return id_name_dict


def group_id_to_name(id_list, group_name):
    """
    asks the api for names to ids then collects into a dict
    for one group at a time

    id_list : list of ids given as ints
    group_name : string (one of [artist, publisher, designer, category, mechanic])

    returns : dictionary

    eg:
    group_id_to_name([100, 150], "publisher")
    """
    id_name_dict = {}
    publishers_string = [str(x) for x in id_list]
    publishers_string = ",".join(publishers_string)
    url = "https://www.boardgamegeek.com/xmlapi/boardgame{}/{}".format(
        group_name, publishers_string
    )
    print(url)
    resp = requests.get(url)
    tree = ET.fromstring(resp.content)
    for idx, val in enumerate(list(tree)):
        name = val.find("name").text
        id = id_list[idx]
        id_name_dict[id] = name
    return id_name_dict


if __name__ == "__main__":
    # url = "https://www.boardgamegeek.com/xmlapi/boardgame/13"
    # resp = requests.get(url)
    # tree = ET.fromstring(resp.content)

    pub_list = [100, 150]
    pubs = group_id_to_name(pub_list, "publisher")
    print(pubs)

    # import pdb

    # pdb.set_trace()

    # print(tree)
