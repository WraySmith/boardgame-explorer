"""
contains graph calls for dashboard
"""

import altair as alt
from wrangling.py import call_boardgame_data


def scatter_plot_dates(cat=None, mech=None, pub=None):
    """
    Takes in inputs filtering data and creates scatter plot
    for comparison of user ratings over time

    cat: string input
    mech: string input
    pub: string input

    returns: altair plot
    """

    scatter_plot = (
        alt.Chart(call_boardgame_data(cat, mech, pub))
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
        alt.Chart(call_boardgame_data(cat, mech, pub))
        .mark_line(color="#1f77b4", size=3)
        .encode(
            x="year_published",
            y="mean(average_rating)",
            opacity=alt.Opacity(
                "Linelabel", legend=alt.Legend(title=None, orient="top-left")
            ),
        )
    )

    return scatter_plot
