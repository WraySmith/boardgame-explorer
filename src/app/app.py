# import functions needed
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_table
import plotly.graph_objs as go

# import functions from .py files
import app_graphing as app_gr
import app_wrangling as app_wr

# load board game data
boardgame_data = app_wr.call_boardgame_data()

# dictionary for tab 1 sliders
max_year = boardgame_data["year_published"].max().year
slider_dict = {x: str(x) for x in range(1950, (max_year + 1), 5)}

# dictionary for dropdowns
col_key_list = ["category", "mechanic", "publisher"]
col_value_list = [app_wr.subset_data(boardgame_data, v) for v in col_key_list]
col_dict = dict(zip(col_key_list, col_value_list))


#  set up app stylesheet and server
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


# title
def title():
    """
    :return: A Div containing dashboard title.
    """
    return html.Div(children=[html.H1("Board Game Trends Dashboard")])


# description card tab 1
def description_card_tab1():
    """
    :return: A Div containing welcome message and descriptions.
    """
    return html.Div(
        id="description-card-tab1",
        children=[
            html.H5("Welcome to our Board Games Dashboard"),
            html.Div(
                id="intro",
                children="Explore board game trends over time based on category, mechanics \
                    and publisher selection below. Also visualize the top categories,\
                    mechanics and publishers by year using our interactive features.",
            ),
        ],
    )


# control card for tab 1
def generate_control_card_tab1():
    """
    :return: A Div containing controls for graphs on tab 1.
    """
    return html.Div(
        id="control-card-tab1",
        children=[
            html.Label("Select what you want to view:"),
            html.Br(),
            html.Br(),
            dcc.RadioItems(
                id="radio-selection-tab1",
                options=[
                    {"label": " Categories", "value": "category"},
                    {"label": " Mechanics", "value": "mechanic"},
                    {"label": " Publishers", "value": "publisher"},
                ],
                value="mechanic",
                labelStyle={"display": "block"},
            ),
            html.Br(),
            html.Label("Select elements to view:"),
            html.Br(),
            html.Br(),
            dcc.Dropdown(
                id="radio-dependent-tab1", options=[], multi=True, value=[None]
            ),
        ],
    )


# control card for tab 2
def generate_control_card_tab2():
    """
    :return: A Div containing controls for graphs on tab 2.
    """
    return html.Div(
        id="control-card-tab2",
        children=[
            html.P(
                "Please select any combination of categories, mechanics, publishers\
                     and number of games to show"
            ),
            html.Br(),
            html.P("Please select categories:"),
            dcc.Dropdown(
                id="category-widget-tab2",
                value="",
                options=[
                    {"label": name, "value": name} for name in col_dict["category"]
                ],
                multi=True,
            ),
            html.Br(),
            html.P("Please select mechanics:"),
            dcc.Dropdown(
                id="mechanics-widget-tab2",
                value="",
                options=[
                    {"label": name, "value": name} for name in col_dict["mechanic"]
                ],
                multi=True,
            ),
            html.Br(),
            html.P("Please select publishers:"),
            dcc.Dropdown(
                id="publisher-widget-tab2",
                value="",
                options=[
                    {"label": name, "value": name} for name in col_dict["publisher"]
                ],
                multi=True,
            ),
            html.Br(),
            html.Br(),
        ],
    )


# control card for tab 3
def generate_control_card_tab3():
    """
    :return: A Div containing controls for graphs on tab 3.
    """
    return html.Div(
        id="control-card-tab3",
        children=[
            html.Label("Select:"),
            html.Br(),
            dcc.RadioItems(
                id="radio-selection-tab3",
                options=[
                    {"label": " Categories", "value": "category"},
                    {"label": " Mechanics", "value": "mechanic"},
                    {"label": " Publishers", "value": "publisher"},
                ],
                value="mechanic",
                labelStyle={"display": "block"},
            ),
            html.Br(),
            html.Label("Select elements to view:"),
            html.Br(),
            dcc.Dropdown(
                id="radio-dependent-tab3", options=[], multi=True, value=[None]
            ),
        ],
    )


# lower description for tab 1
def lower_description_tab1():
    """
    :return: A Div containing description for lower portion of tab 1.
    """
    return html.Div(
        children=[
            html.H4("Top 5 Categories, Mechanics and Publishers by Rating"),
            html.P(
                "Two sets of bar charts with year range sliders are provided \
                    to allow comparison for two different periods.",
            ),
            html.Br(),
            html.P(
                "Drag the year sliders below to select your year ranges and \
                    compare the top 5 categories, mechanics and publishers \
                    between time periods."
            ),
        ]
    )


# data set description for tab 1
def data_set_description_tab1():
    """
    :return: A Div containing description of the data set for tab 1.
    """
    return html.Div(
        children=[
            html.H4("Description of Dataset"),
            html.P(
                " This dataset comes from the Board Game Geek website and \
                    includes boardgames with descriptions, general game \
                    details, publisher, and user ratings for 10,000 boardgames\
                    published between 1950 and 2021."
            ),
        ]
    )


# below are the cards that are used in the layout


# card 1 containing the description and control card for tab 1
first_card_tab1 = dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                id="left-upper-tab1",
                className="four columns",  # not sure this is needed?
                children=[
                    description_card_tab1(),
                    html.Br(),
                    generate_control_card_tab1(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                ],
            )
        ]
    )
)
# card 2 containing the two plots on upper portion of tab 1,
# the scatter plot and the counts stacked histogram
second_card_tab1 = dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                [
                    html.H4("Board Game Ratings and Counts from 1950 to 2016"),
                    html.P(
                        "Select either categories, mechanics or publishers.\
                             Then select different elements to view on the\
                                following two figures."
                    ),
                    html.Iframe(
                        # scatter plot
                        id="scatter",
                        style={
                            "border-width": "0",
                            "width": "100%",
                            "height": "250px",
                        },
                    ),
                    html.Iframe(
                        # stacked histogram
                        id="count",
                        style={
                            "border-width": "0",
                            "width": "100%",
                            "height": "250px",
                        },
                    ),
                ]
            ),
            html.Br(),
        ]
    )
)


# card 3 containing the lower description and
# collapsable data set description for tab 1
third_card_tab1 = dbc.Card(
    dbc.CardBody(
        [
            dbc.Col(
                id="left-lower-tab1",
                className="four columns",  # not sure this is needed?
                children=[lower_description_tab1()],
            )
        ]
    )
)


# card 4 containing the top slider and bar charts to view top categories,
# mechanics and publishers for selected time periods from the slider for tab 1
fourth_card_tab1 = dbc.Card(
    dbc.CardBody(
        [
            dbc.Row(
                [
                    html.Div(
                        [
                            html.Div(
                                id="top-range-slider-output",
                                style={"align-items": "center"},
                            ),
                            html.Br(),
                            html.Br(),
                            dcc.RangeSlider(
                                id="top-range-slider",
                                min=1950,
                                max=2016,
                                step=1,
                                value=[1990, 2010],
                                marks=slider_dict,
                            ),
                            html.Br(),
                            html.Iframe(
                                id="top-barcharts",
                                style={
                                    "border-width": "0",
                                    "width": "1050px",
                                    "height": "200px",
                                },
                            ),
                            html.Br(),
                            html.Br(),
                        ]
                    )
                ]
            )
        ]
    )
)


# card 5 containing the bottom slider and bar charts to view top categories,
# mechanics and publishers for selected time periods from the slider for tab 1
fifth_card_tab1 = dbc.Card(
    dbc.CardBody(
        [
            dbc.Row(
                [
                    html.Div(
                        [
                            html.Div(id="bottom-range-slider-output"),
                            html.Br(),
                            html.Br(),
                            dcc.RangeSlider(
                                id="bottom-range-slider",
                                min=1950,
                                max=2016,
                                step=1,
                                value=[1990, 2010],
                                marks=slider_dict,
                            ),
                            html.Br(),
                            html.Iframe(
                                id="bottom-barcharts",
                                style={
                                    "border-width": "0",
                                    "width": "1050px",
                                    "height": "200px",
                                },
                            ),
                            html.Br(),
                            html.Br(),
                        ]
                    )
                ]
            )
        ]
    )
)


# card 6 containing the control card and the slider for number of games for tab 2
sixth_card_tab2 = dbc.Card(dbc.CardBody([generate_control_card_tab2()]))


# card 7 containing the top 10 games bar chart for tab 2
seventh_card_tab2 = dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                html.Iframe(
                    id="top-n-games",
                    style={"border-width": "0", "width": "100%", "height": "300px"},
                )
            )
        ]
    )
)


# card 8 containing the data table for the top n games for tab 2
eight_card_tab2 = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Top 10 Games Facts Table:"),
            dash_table.DataTable(
                id="top-n-games-datatable",
                style_cell={"whiteSpace": "normal", "height": "auto"},
                style_table={"overflowY": "scroll"},
                sort_action="native",
            ),
        ]
    )
)


# card 9 for data set description tab 1
ninth_card_tab1 = dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                [
                    dbc.Button(
                        "Click here to view dataset description",
                        id="collapse-button",
                        className="mb-3",  # not sure this is needed
                        color="primary",
                    ),
                    dbc.Collapse(
                        dbc.Card(dbc.CardBody(data_set_description_tab1())),
                        id="collapse",
                    ),
                ]
            )
        ]
    )
)


# card 10 containing the control card for tab 3
tenth_card_tab3 = dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                id="left-column-tab3",
                className="four columns",  # not sure this is needed
                children=[
                    generate_control_card_tab3(),
                ],
            )
        ]
    )
)


# card 11 containing the tsne plot on tab 3,
tsne_layout = go.Layout(margin=dict(l=0, r=0, b=0, t=0), title=dict(text="test"))
eleventh_card_tab3 = dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                [
                    html.H4("Board Game Explorer"),
                    html.P(
                        "Select either categories, mechanics or publishers.\
                             Then select different elements to view on the\
                                following figure."
                    ),
                    dcc.Graph(id="tsne-3d-plot", style={"height": "80vh"}),
                ]
            ),
            html.Br(),
        ]
    )
)


# tab styling features for layout
tabs_styles = {"height": "44px" ""}
tab_style = {
    "borderBottom": "1px solid #d6d6d6",
    "padding": "6px",
    "fontWeight": "bold",
}

tab_selected_style = {
    "borderTop": "1px solid #d6d6d6",
    "borderBottom": "1px solid #d6d6d6",
    "backgroundColor": "#119DFF",
    "color": "white",
    "padding": "6px",
}


# app layout
app.layout = html.Div(
    [
        dbc.Container(
            [  # dashboard title
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div(
                                    id="title-top",
                                    className="title on top",  # needed?
                                    children=[title()],
                                )
                            ],
                            width=12,
                        )
                    ]
                )
            ]
        ),
        dcc.Tabs(
            [
                # tab 1
                dcc.Tab(
                    label="Game Trends",
                    children=[
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(first_card_tab1, width=3),
                                dbc.Col(second_card_tab1, width=9),
                            ]
                        ),
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [third_card_tab1, html.Br(), ninth_card_tab1],
                                    width=3,
                                ),
                                dbc.Col(
                                    [(fourth_card_tab1), html.Br(), (fifth_card_tab1)],
                                    width=9,
                                ),
                            ],
                        ),
                    ],
                    style=tab_style,
                    selected_style=tab_selected_style,
                ),
                # tab 2
                dcc.Tab(
                    label="Top Games",
                    children=[
                        dbc.Container(
                            [
                                html.Br(),
                                dbc.Row(
                                    [
                                        dbc.Col(sixth_card_tab2, width=3),
                                        dbc.Col(
                                            [
                                                (seventh_card_tab2),
                                                html.Br(),
                                                (eight_card_tab2),
                                            ],
                                            width=9,
                                            style={"height": "100vh"},
                                        ),
                                    ]
                                ),
                            ]
                        )
                    ],
                    style=tab_style,
                    selected_style=tab_selected_style,
                ),
                # tab 3
                dcc.Tab(
                    label="Game Explorer",
                    children=[
                        html.Br(),
                        dbc.Row(
                            [
                                dbc.Col(tenth_card_tab3, width=3),
                                dbc.Col(eleventh_card_tab3, width=9),
                            ]
                        ),
                        html.Br(),
                    ],
                    style=tab_style,
                    selected_style=tab_selected_style,
                ),
            ]
        ),
    ]
)


# Set up callbacks/backend

# radio button selection options to populate drop downs for tab1
@app.callback(
    dash.dependencies.Output("radio-dependent-tab1", "options"),
    [dash.dependencies.Input("radio-selection-tab1", "value")],
)
def update_options(chosen_selection):
    col = chosen_selection
    return [{"label": c, "value": c} for c in col_dict[col]]


# radio button selection options to populate drop downs for tab3
@app.callback(
    dash.dependencies.Output("radio-dependent-tab3", "options"),
    [dash.dependencies.Input("radio-selection-tab3", "value")],
)
def update_options(chosen_selection):
    col = chosen_selection
    return [{"label": c, "value": c} for c in col_dict[col]]


# scatter plot tab 1
@app.callback(
    Output("scatter", "srcDoc"),
    Input("radio-selection-tab1", "value"),
    Input("radio-dependent-tab1", "value"),
)
def call_scatter(col, list_):
    chart = app_gr.scatter_plot_dates(boardgame_data, col, list_)
    return chart.to_html()


# stacked histogram of counts annual published counts
@app.callback(
    Output("count", "srcDoc"),
    Input("radio-selection-tab1", "value"),
    Input("radio-dependent-tab1", "value"),
)
def call_counts(col, list_):
    chart2 = app_gr.count_plot_dates(boardgame_data, col, list_)
    return chart2.to_html()


# 1st facet chart
@app.callback(
    Output("top-barcharts", "srcDoc"),
    Input("top-range-slider", "value"),
)
def update_output1(value):
    transformed_value = [v for v in value]
    val1 = transformed_value[0]
    val2 = transformed_value[1]
    hist1 = app_gr.rank_plot_facet(
        data=boardgame_data, year_in=int(val1), year_out=int(val2)
    )
    return hist1.to_html()


# 2nd facet chart
@app.callback(
    Output("bottom-barcharts", "srcDoc"),
    Input("bottom-range-slider", "value"),
)
def update_output2(value):
    transformed_value = [v for v in value]
    val1 = transformed_value[0]
    val2 = transformed_value[1]
    hist2 = app_gr.rank_plot_facet(
        data=boardgame_data, year_in=int(val1), year_out=int(val2)
    )
    return hist2.to_html()


# 1st year range slider output tab 1
@app.callback(
    dash.dependencies.Output("top-range-slider-output", "children"),
    dash.dependencies.Input("top-range-slider", "value"),
)
def range_slider_select(value):
    transformed_value = [v for v in value]
    return "Years Selected: {} to {}".format(transformed_value[0], transformed_value[1])


# 2nd year range slider output tab 1
@app.callback(
    dash.dependencies.Output("bottom-range-slider-output", "children"),
    dash.dependencies.Input("bottom-range-slider", "value"),
)
def range_slider_select2(value):
    transformed_value = [v for v in value]
    return "Years Selected: {} to {}".format(transformed_value[0], transformed_value[1])


# collapsable data set description
@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


# top n games bar chart tab 2
@app.callback(
    Output("top-n-games", "srcDoc"),
    Input("category-widget-tab2", "value"),
    Input("mechanics-widget-tab2", "value"),
    Input("publisher-widget-tab2", "value"),
)
def call_top_n_games(c, m, p, n=10):
    top_n_games = app_gr.top_n_plot(data=boardgame_data, cat=c, mech=m, pub=p, n=10)
    return top_n_games.to_html()


# data table top n games bar chart tab 2
@app.callback(
    Output("top-n-games-datatable", "data"),
    Output(component_id="top-n-games-datatable", component_property="columns"),
    Input("category-widget-tab2", "value"),
    Input("mechanics-widget-tab2", "value"),
    Input("publisher-widget-tab2", "value"),
)
def update_table(c, m, p, n=10):
    list_cols = [
        "name",
        "min_players",
        "max_players",
        "min_playtime",
        "max_playtime",
        "year_published",
        "category",
        "mechanic",
        "publisher",
        "average_rating",
        "users_rated",
    ]
    table = app_wr.call_boardgame_filter(
        data=boardgame_data, cat=c, mech=m, pub=p, n=10
    )
    columns = [{"name": col, "id": col} for col in list_cols]
    columns[0]["name"] = ("Game name",)
    columns[1]["name"] = "Min Players"
    columns[2]["name"] = "Max Players"
    columns[3]["name"] = "Min Playtime"
    columns[4]["name"] = "Max Playtime"
    columns[5]["name"] = "Year Published"
    columns[6]["name"] = "Game Category"
    columns[7]["name"] = "Game Mechanic"
    columns[8]["name"] = "Game Publisher"
    columns[9]["name"] = "Average Game Rating"
    columns[10]["name"] = "User Rating"

    data = table.to_dict("rows")
    return data, columns


# tsne graph tab 3
@app.callback(
    Output("tsne-3d-plot", "figure"),
    Input("radio-selection-tab3", "value"),
    Input("radio-dependent-tab3", "value"),
)
def call_tsne(col, list_):
    data = app_gr.graph_3D(boardgame_data, col, list_)
    fig = {"data": data, "layout": tsne_layout}
    return fig


# run
if __name__ == "__main__":
    app.run_server(debug=True, host="127.0.0.1", port=8055)
