import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd

from functions import *
from wrangling import subset_data


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


# left most


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


# layout
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
                                                    id="top-row",
                                                    className="four columns",
                                                    children=[title()],
                                                )
                                            ],
                                            width=12,
                                        )
                                    ]
                                ),
                                html.Br(),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                html.Div(
                                                    id="left-column",
                                                    className="four columns",
                                                    children=[
                                                        description_card(),
                                                        generate_control_card(),
                                                    ],
                                                )
                                            ],
                                            width=3,
                                        ),
                                        dbc.Col(
                                            [
                                                html.Div(
                                                    [
                                                        html.H4(
                                                            "Board game ratings and counts from 1950 to 2016"
                                                        ),
                                                        html.P(
                                                            "Select multiple categories, mechanics and publishers on the left hand side dropdown menus to view..."
                                                        ),
                                                        html.Iframe(
                                                            id="scatter",
                                                            style={
                                                                "border-width": "0",
                                                                "width": "100%",
                                                                "height": "250px",
                                                            },
                                                        ),
                                                        html.Iframe(
                                                            # will be the counts graph
                                                            id="count",
                                                            style={
                                                                "border-width": "0",
                                                                "width": "100%",
                                                                "height": "250px",
                                                            },
                                                        ),
                                                    ]
                                                )
                                            ],
                                            width=9,
                                        ),
                                    ]
                                ),
                                dbc.Row(
                                    [
                                        (
                                            dbc.Col(
                                                id="bottom left row",
                                                className="four columns",
                                                children=[lower_description()],
                                            )
                                        ),
                                        html.Div(
                                            html.Iframe(
                                                id="output-container-range-slider-non-linear",
                                                style={
                                                    "border-width": "0",
                                                    "width": "100%",
                                                    "height": "250px",
                                                },
                                            ),
                                        ),
                                        html.Div(
                                            html.Iframe(
                                                id="output-container-range-slider-non-linear2",
                                                style={
                                                    "border-width": "0",
                                                    "width": "100%",
                                                    "height": "250px",
                                                },
                                            ),
                                        ),
                                        html.Div(
                                            html.Iframe(
                                                id="output-container-range-slider-non-linear3",
                                                style={
                                                    "border-width": "0",
                                                    "width": "100%",
                                                    "height": "250px",
                                                },
                                            ),
                                        ),
                                    ],
                                ),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            id="bbc",
                                            className="four columns",
                                            children=[()],
                                            width=3,
                                        ),
                                        dbc.Col(
                                            [
                                                dcc.RangeSlider(
                                                    id="non-linear-range-slider",
                                                    min=1950,
                                                    max=2016,
                                                    step=1,
                                                    value=[1990, 2010],
                                                    marks={
                                                        1950: "1950",
                                                        1955: "1955",
                                                        1960: "1960",
                                                        1965: "1965",
                                                        1970: "1970",
                                                        1975: "1975",
                                                        1980: "1980",
                                                        1985: "1985",
                                                        1990: "1990",
                                                        1995: "1995",
                                                        2000: "2000",
                                                        2005: "2005",
                                                        2010: "2010",
                                                        2015: "2015",
                                                    },
                                                )
                                            ]
                                        ),
                                    ]
                                ),
                                dbc.Row(
                                    [
                                        (
                                            dbc.Col(
                                                id="bb",
                                                className="four columns",
                                                children=[data_set_descirption()],
                                            )
                                        ),
                                        html.Div(
                                            html.Iframe(
                                                id="output-container-range-slider-non-linear4",
                                                style={
                                                    "border-width": "0",
                                                    "width": "100%",
                                                    "height": "250px",
                                                },
                                            ),
                                        ),
                                        html.Div(
                                            html.Iframe(
                                                id="output-container-range-slider-non-linear5",
                                                style={
                                                    "border-width": "0",
                                                    "width": "100%",
                                                    "height": "250px",
                                                },
                                            ),
                                        ),
                                        html.Div(
                                            html.Iframe(
                                                id="output-container-range-slider-non-linear6",
                                                style={
                                                    "border-width": "0",
                                                    "width": "100%",
                                                    "height": "250px",
                                                },
                                            ),
                                        ),
                                    ],
                                ),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            id="bbcc",
                                            className="four columns",
                                            children=[()],
                                            width=3,
                                        ),
                                        dbc.Col(
                                            [
                                                dcc.RangeSlider(
                                                    id="non-linear-range-slider2",
                                                    min=1950,
                                                    max=2016,
                                                    step=1,
                                                    value=[1990, 2010],
                                                    marks={
                                                        1950: "1950",
                                                        1955: "1955",
                                                        1960: "1960",
                                                        1965: "1965",
                                                        1970: "1970",
                                                        1975: "1975",
                                                        1980: "1980",
                                                        1985: "1985",
                                                        1990: "1990",
                                                        1995: "1995",
                                                        2000: "2000",
                                                        2005: "2005",
                                                        2010: "2010",
                                                        2015: "2015",
                                                    },
                                                )
                                            ]
                                        ),
                                    ]
                                ),
                            ]
                        )
                    ],
                ),
                dcc.Tab(label="Tab two", children=[]),
            ]
        )
    ]
)


# Set up callbacks/backend
# will be the scatteplot of average game ratings
@app.callback(
    Output("scatter", "srcDoc"),
    Input("category-widget", "value"),
    Input("mechanics-widget", "value"),
    Input("publisher-widget", "value"),
)
def call_scatter(c, m, p):
    chart = scatter_plot_dates(cat=c, mech=m, pub=p)
    return chart.to_html()


# histogram of counts annual published counts
@app.callback(
    Output("count", "srcDoc"),
    Input("category-widget", "value"),
    Input("mechanics-widget", "value"),
    Input("publisher-widget", "value"),
)
def call_counts(c, m, p):
    chart2 = count_plot_dates(cat=c, mech=m, pub=p)
    return chart2.to_html()


@app.callback(
    Output("output-container-range-slider-non-linear", "srcDoc"),
    Input("non-linear-range-slider", "value"),
)
def update_output(value):
    transformed_value = [v for v in value]
    val1 = transformed_value[0]
    val2 = transformed_value[1]
    hist1 = rank_plot_dates(
        col="category", year_in=int(val1), year_out=int(val2), color_="#ff7f0e"
    )
    return hist1.to_html()


@app.callback(
    Output("output-container-range-slider-non-linear2", "srcDoc"),
    Input("non-linear-range-slider", "value"),
)
def update_output2(value):
    transformed_value = [v for v in value]
    val1 = transformed_value[0]
    val2 = transformed_value[1]
    hist2 = rank_plot_dates(
        col="mechanic", year_in=int(val1), year_out=int(val2), color_="#17becf"
    )
    return hist2.to_html()


@app.callback(
    Output("output-container-range-slider-non-linear3", "srcDoc"),
    Input("non-linear-range-slider", "value"),
)
def update_output3(value):
    transformed_value = [v for v in value]
    val1 = transformed_value[0]
    val2 = transformed_value[1]
    hist3 = rank_plot_dates(
        col="publisher", year_in=int(val1), year_out=int(val2), color_="#e377c2"
    )
    return hist3.to_html()


@app.callback(
    Output("output-container-range-slider-non-linear4", "srcDoc"),
    Input("non-linear-range-slider2", "value"),
)
def update_output4(value):
    transformed_value = [v for v in value]
    val1 = transformed_value[0]
    val2 = transformed_value[1]
    hist4 = rank_plot_dates(
        col="category", year_in=int(val1), year_out=int(val2), color_="#ff7f0e"
    )
    return hist4.to_html()


@app.callback(
    Output("output-container-range-slider-non-linear5", "srcDoc"),
    Input("non-linear-range-slider2", "value"),
)
def update_output5(value):
    transformed_value = [v for v in value]
    val1 = transformed_value[0]
    val2 = transformed_value[1]
    hist5 = rank_plot_dates(
        col="mechanic", year_in=int(val1), year_out=int(val2), color_="#17becf"
    )
    return hist5.to_html()


@app.callback(
    Output("output-container-range-slider-non-linear6", "srcDoc"),
    Input("non-linear-range-slider2", "value"),
)
def update_output6(value):
    transformed_value = [v for v in value]
    val1 = transformed_value[0]
    val2 = transformed_value[1]
    hist6 = rank_plot_dates(
        col="publisher", year_in=int(val1), year_out=int(val2), color_="#e377c2"
    )
    return hist6.to_html()


# run
if __name__ == "__main__":
    app.run_server(debug=True, host="127.0.0.1", port=8053)
