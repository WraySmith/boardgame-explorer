"""
contains graph calls for dashboard
"""

import altair as alt
from wrangling import call_boardgame_filter, call_boardgame_top


def scatter_plot_dates(cat=None, mech=None, pub=None):
    """
    Takes in inputs filtering data and creates scatter plot
    for comparison of user ratings over time

    cat: list of strings input
    mech: list of strings input
    pub: list of strings input

    returns: altair plot
    """

    scatter_plot = (
        alt.Chart(call_boardgame_filter(cat, mech, pub))
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
            width=700,
            height=200,
        )
    )
    scatter_plot = scatter_plot + (
        alt.Chart(call_boardgame_filter(cat, mech, pub))
        .mark_line(color="#1f77b4", size=3)
        .encode(x="year_published", y="mean(average_rating)"),
    )

    return scatter_plot


def count_plot_dates(cat=None, mech=None, pub=None):
    """
    Takes input filtering data and creates
    a plot counting how many game occurances

    cat: list of strings input
    mech: list of strings input
    pub: list of strings input

    return: altair plot
    """
    count_plot = (
        alt.Chart(call_boardgame_filter(cat, mech, pub))
        .mark_bar(color="#2ca02c")
        .encode(
            alt.X(
                "year_published", axis=alt.Axis(title=None), scale=alt.Scale(zero=False)
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
        .properties(width=700, height=200)
    )

    return count_plot


def rank_plot_dates(col="category", year_in=1900, year_out=2020, color_="#ff7f0e"):
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
                axis=alt.Axis(
                    titleFontSize=12,
                    titleFontWeight=600,
                ),
            ),
            alt.Y("average_rating:Q", sort="-x"),
        )
        .properties(width=700, height=200)
    )
    return rank_plot
