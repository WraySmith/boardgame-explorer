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


if __name__ == "__main__":
    # url = "https://www.boardgamegeek.com/xmlapi/boardgame/13"
    # resp = requests.get(url)
    # tree = ET.fromstring(resp.content)

    pub_list = [100, 150]
    pubs = get_publisher_id_name_dict(pub_list)
    print(pubs)

    # import pdb

    # pdb.set_trace()

    # print(tree)
