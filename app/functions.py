"""
contains graph calls for dashboard
"""

import altair as alt
from wrangling import *


def scatter_plot_dates(col="category", list_=[None]):
    """
    Takes in inputs filtering data and creates scatter plot
    for comparison of user ratings over time

    col: string
    dict_: dictionary

    returns: altair plot
    """
    alt.data_transformers.disable_max_rows()

    scatter_plot = (
        alt.Chart(call_boardgame_data())
        .mark_circle(size=60, opacity=0.1, color="grey")
        .encode(
            alt.X(
                "year_published", axis=alt.Axis(title=None), scale=alt.Scale(zero=False)
            ),
            alt.Y(
                "average_rating",
                axis=alt.Axis(
                    title="Average Rating",
                    titleFontSize=12,
                    offset=14,
                    titleFontWeight=600,
                ),
            ),
        )
        .properties(
            title=alt.TitleParams(
                text="Figure 1: Game Popularity based on Published Year",
                anchor="start",
                fontSize=20,
                dy=-20,
                dx=20,
            ),
            width=650,
            height=150,
        )
    )

    line_plot = (
        alt.Chart(call_boardgame_data())
        .mark_line(color="dark grey", size=3)
        .encode(x="year_published", y="mean(average_rating)")
    )

    color_plot = (
        alt.Chart(call_boardgame_radio(col, list_))
        .mark_circle(size=60, opacity=0.5, color="orange")
        .encode(
            alt.X(
                "year_published", axis=alt.Axis(title=None), scale=alt.Scale(zero=False)
            ),
            alt.Y(
                "average_rating",
                axis=alt.Axis(
                    title="Average Rating",
                    titleFontSize=12,
                    offset=14,
                    titleFontWeight=600,
                ),
            ),
            color=alt.Color("group", title="Group"),
        )
        .properties(
            title=alt.TitleParams(
                text="Figure 1: Game Popularity based on Published Year",
                anchor="start",
                fontSize=20,
                dy=-20,
                dx=20,
            ),
            width=650,
            height=150,
        )
    )

    if list_ == [None]:
        scatter_plot = scatter_plot + line_plot
    else:
        scatter_plot = color_plot + line_plot
    return scatter_plot


def count_plot_dates(col="category", list_=[None]):
    """
    Takes input filtering data and creates
    a plot counting how many game occurances

    col: string
    list_: list of strings input

    return: altair plot
    """
    # list_ = dict_to_list(dict_)

    if list_ != [None]:
        alt.data_transformers.disable_max_rows()
        count_plot = (
            alt.Chart(call_boardgame_radio(col, list_))
            .mark_bar(color="#2ca02c")
            .encode(
                alt.X(
                    "year_published",
                    axis=alt.Axis(title=None),
                    scale=alt.Scale(zero=False),
                ),
                alt.Y(
                    "count()",
                    axis=alt.Axis(
                        title="Count of Games Published",
                        titleFontSize=12,
                        offset=8,
                        titleFontWeight=600,
                    ),
                ),
                color=alt.Color("group", title="Group"),
            )
            .properties(
                title=alt.TitleParams(
                    text="Figure 2: Game Count based on Published Year",
                    anchor="start",
                    fontSize=20,
                    dy=-20,
                    dx=20,
                ),
                width=650,
                height=150,
            )
        )

        return count_plot
    else:
        alt.data_transformers.disable_max_rows()
        count_plot = (
            alt.Chart(call_boardgame_data())
            .mark_bar(color="#2ca02c")
            .encode(
                alt.X(
                    "year_published",
                    axis=alt.Axis(title=None),
                    scale=alt.Scale(zero=False),
                ),
                alt.Y(
                    "count()",
                    axis=alt.Axis(
                        title="Count of Games Published",
                        titleFontSize=12,
                        offset=8,
                        titleFontWeight=600,
                    ),
                ),
            )
            .properties(
                title=alt.TitleParams(
                    text="Figure 2: Game Count based on Published Year",
                    anchor="start",
                    fontSize=20,
                    dy=-20,
                    dx=20,
                ),
                width=650,
                height=150,
            )
        )

        return count_plot


def rank_plot_dates(col="category", year_in=1990, year_out=2010, color_="#ff7f0e"):
    """
    Creates altair graph of set column for set years

    col: string
    year_in: int
    year_out: int

    return: altair plot
    """
    rank_plot = (
        alt.Chart(call_boardgame_top(col, year_in, year_out))
        .mark_bar(color=color_)
        .encode(
            alt.X(
                str(col),
                sort="-y",
                axis=alt.Axis(
                    titleFontSize=12,
                    titleFontWeight=600,
                ),
            ),
            alt.Y(
                "average_rating:Q",
                axis=alt.Axis(title="Average Rating"),
                scale=alt.Scale(domain=(5, 10)),
            ),
        )
        .properties(width=200, height=100)
    )

    rank_text = rank_plot.mark_text(align="center", baseline="bottom", dy=-3).encode(
        text=alt.Text("average_rating:Q", format=",.2r")
    )
    return rank_plot + rank_text


def top_n_plot(cat=[None], mech=[None], pub=[None], n=5):
    """
    Creates altair graph for top "n" games with filtered data

    cat: list
    mech: list
    pub: list
    n: int

    return: altair plot
    """
    alt.data_transformers.disable_max_rows()
    top_plot = (
        alt.Chart(call_boardgame_filter(cat, mech, pub, n))
        .mark_bar()
        .encode(
            alt.X(
                "name",
                sort="-y",
                axis=alt.Axis(title=None, labels=False),
            ),
            alt.Y(
                "average_rating:Q",
                axis=alt.Axis(title="Average Rating"),
                scale=alt.Scale(domain=(0, 10)),
            ),
            color=alt.Color("name", title="Boardgame Name"),
        )
        .properties(
            title=alt.TitleParams(
                text="Figure 1: Top n games based on user selection",
                anchor="start",
                fontSize=20,
                dy=-20,
                dx=20,
            ),
            width=500,
            height=150,
        )
    )
    top_text = top_plot.mark_text(align="center", baseline="bottom", dy=-3).encode(
        text=alt.Text("average_rating:Q", format=",.2r")
    )

    return top_plot + top_text
