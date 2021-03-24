"""
hold util functions for api queriering
"""


def create_chunks(id_list, n):
    """
    breaks list into chunks of length n

    id_list: list of ints that are strings
    n: int

    returns: generator of lists
    """

    for i in range(0, len(id_list), n):
        yield id_list[i : i + n]


# TODO this will eventually include a "load the latest dataset function"
