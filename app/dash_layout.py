import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd

from functions import *
from wrangling import subset_data


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


def title():
    return html.Div(children=[html.H1("Boardgames Trends Dashboard")])


def description_card():
    """
    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card",
        children=[
            html.H5("Welcome to our Boardgames Dashboard"),
            html.Div(
                id="intro",
                children="Explore boardgame trends over time based on category, mechanics and publisher selection below. Also visualize the top categories, mechanics and publishers by year using our interactive features.",
            ),
        ],
    )


# left most
def generate_control_card():
    """
    :return: A Div containing controls for graphs.
    """
    return html.Div(
        id="control-card",
        children=[
            html.Br(),
            html.Br(),
            html.P("Please select categories:"),
            dcc.Dropdown(
                id="category-widget",
                value="Economic",
                options=[
                    {"label": name, "value": name} for name in subset_data("category")
                ],
                multi=True,
            ),
            html.Br(),
            html.Br(),
            html.P("Please select mechanics:"),
            dcc.Dropdown(
                id="mechanics-widget",
                value="Trick-taking",
                options=[
                    {"label": name, "value": name} for name in subset_data("mechanic")
                ],
                multi=True,
            ),
            html.Br(),
            html.Br(),
            html.P("Please select publishers:"),
            dcc.Dropdown(
                id="publisher-widget",
                value="3M",
                options=[
                    {"label": name, "value": name} for name in subset_data("publisher")
                ],
                multi=True,
            ),
            html.Br(),
            html.Br(),
        ],
    )


def lower_description():
    return html.Div(
        children=[
            html.H4("Top 5 categories, mechanics and publishers by rating"),
            html.P(
                "Drag the year sliders below to select your year ranges and compare the top 5 categories, mechanics and publishers between time periods"
            ),
        ]
    )


def data_set_descirption():
    return html.Div(
        children=[
            html.H4("Description of Dataset"),
            html.P(
                " This dataset comes from the Board Game Geek website and includes boardgames with descriptions, general game details, publisher, and user ratings for 10,000 boardgames published between 1950 and 2021"
            ),
        ]
    )


app.layout = html.Div(
    [
        dcc.Tabs(
            [
                dcc.Tab(
                    label="Tab one",
                    children=[
                        dbc.Container(
                            [  # top column
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                html.Div(
                                                    id="title_top",
                                                    className="title on top",
                                                    children=[title()],
                                                )
                                            ],
                                            width=12,
                                        )
                                    ]
                                )
                            ]
                        )
                    ],

html.Div(
    [
                    dbc.Card(
    dbc.CardBody(
        [
            html.H4("Title", className="card-title"),
            html.H6("Card subtitle", className="card-subtitle"),
            html.P(
                "Some quick example text to build on the card title and make "
                "up the bulk of the card's content.",
                className="card-text",
            ),
            dbc.CardLink("Card link", href="#"),
            dbc.CardLink("External link", href="https://google.com"),
        ]
    ),
    style={"width": "18rem"},
)
                )
            ]
        )
    ]
)


# run
if __name__ == "__main__":
    app.run_server(debug=True, host="127.0.0.1", port=8055)
