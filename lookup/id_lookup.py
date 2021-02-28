"""
working with the bgg api
eg:
https://www.boardgamegeek.com/xmlapi/boardgame/13,150
"""

import requests
import xml.etree.ElementTree as ET


def group_id_to_name(id_list, group_name):
    """
    asks the api for names to ids then collects into a dict
    for one group at a time

    id_list : list of ids given as ints
    group_name : string (one of [artist, publisher,
                                 designer, category, mechanic, game])

    returns : dictionary

    eg:
    group_id_to_name([100, 150], "publisher")
    """
    id_name_dict = {}
    publishers_string = [str(x) for x in id_list]
    publishers_string = ",".join(publishers_string)
    url = "https://www.boardgamegeek.com/xmlapi/boardgame"
    if group_name != "game":
        url = url + group_name
    url += "/{}".format(publishers_string)
    print(url)
    resp = requests.get(url)
    try:
        tree = ET.fromstring(resp.content)
    except:
        print(resp.content)
    for idx, val in enumerate(list(tree)):
        name = val.find("name").text
        id = id_list[idx]
        id_name_dict[id] = name
    return id_name_dict


if __name__ == "__main__":
    # url = "https://www.boardgamegeek.com/xmlapi/boardgame/13"
    # resp = requests.get(url)
    # tree = ET.fromstring(resp.content)

    pub_list = [13, 150]
    pubs = group_id_to_name(pub_list, "game")
    print(pubs)

    # import pdb

    # pdb.set_trace()

    # print(tree)
