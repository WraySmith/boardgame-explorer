"""
hold util functions for creating the look up tables
"""


def extract_ids_from_column(column):
    """
    ids in the column exist as ints or lists of ints

    column: pandas series

    returns: flat list of ints
    """

    st = column.astype("str", copy=False).dropna(
        inplace=False
    )  # some columns were mixed type

    strings = st.map(lambda x: x.split(","))
    id_list = set(strings.explode().values)
    return list(id_list)


def create_chunks(id_list, n):
    """
    breaks list into chunks of length n

    id_list: list of ints that are strings
    n: int

    returns: generator of lists
    """

    for i in range(0, len(id_list), n):
        yield id_list[i : i + n]
