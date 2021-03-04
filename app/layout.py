import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import altair as alt
from vega_datasets import data
import dash_bootstrap_components as dbc


# read in dummy data for layout
cars = data.cars()

# create the dash components using functions


def description_card():
    """
    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card",
        children=[
            html.H5("Boardgames Dashboard"),
            html.H3("Welcome to our Boardgames Dashboard"),
            html.Div(
                id="intro",
                children="Explore ..................................",
            ),
        ],
    )


def generate_control_card():
    """
    :return: A Div containing controls for graphs.
    """
    return html.Div(
        id="control-card",
        children=[
            html.P("Select a Category"),
            dcc.Dropdown(
                id="category-widget",
                value="Horsepower",
                options=[{"label": col, "value": col} for col in cars.columns],
                multi=True,
            ),
            html.Br(),
            html.P("Select Mechanics"),
            dcc.Dropdown(
                id="mechanics-widget",
                value="Displacement",
                options=[{"label": col, "value": col} for col in cars.columns],
            ),
            html.Br(),
            html.Br(),
            html.P("Select Pulishers"),
            dcc.Dropdown(
                id="publisher-widget",
                value="Displacement",
                options=[{"label": col, "value": col} for col in cars.columns],
            ),
            html.Br(),
            html.Div(
                id="reset-btn-outer",
                children=html.Button(id="reset-btn", children="Reset", n_clicks=0),
            ),
        ],
    )


# Setup app and layout/frontend
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = (
    dbc.Container(
        [  # Left column
            html.Div(
                id="left-column",
                className="four columns",
                children=[description_card(), generate_control_card()],
                style={"border-width": "0", "width": "200px", "height": "400px"},
            ),
            dbc.Col(
                [
                    html.H4("Title"),
                    html.P("Description for user interaction"),
                    html.Iframe(
                        id="scatter",
                        style={"border-width": "0", "width": "100%", "height": "400px"},
                    ),
                    html.Iframe(
                        # will be the counts graph
                        id="count",
                        style={"border-width": "0", "width": "100%", "height": "400px"},
                    ),
                ]
            ),
        ]
    ),
)
dbc.Row(
    [
        dbc.Col([html.H4("Description"), html.P("Description paragraph")]),
        dbc.Col(
            [
                html.H4("Top Ranked Games"),
                html.Iframe(
                    id="bar1",
                    style={"border-width": "0", "width": "100%", "height": "400px"},
                ),
                html.Iframe(
                    id="bar4",
                    style={"border-width": "0", "width": "100%", "height": "400px"},
                ),
            ]
        ),
        dbc.Col(
            [
                html.Iframe(
                    id="bar2",
                    style={"border-width": "0", "width": "100%", "height": "400px"},
                ),
                html.Iframe(
                    id="bar5",
                    style={"border-width": "0", "width": "100%", "height": "400px"},
                ),
            ]
        ),
        dbc.Col(
            [
                html.Iframe(
                    id="bar3",
                    style={"border-width": "0", "width": "100%", "height": "400px"},
                ),
                html.Iframe(
                    id="bar6",
                    style={"border-width": "0", "width": "100%", "height": "400px"},
                ),
            ]
        ),
    ]
),


# Set up callbacks/backend
# will be the scatteplot of average game ratings
@app.callback(
    Output("scatter", "srcDoc"),
    Input("category-widget", "value"),
    Input("mechanics-widget", "value")
    # add for publisher widget
    # ,Input('publisher-widget', 'value')
)
def plot_altair(xcol, ycol):
    chart = (
        alt.Chart(cars)
        .mark_point()
        .encode(x=xcol, y=ycol, tooltip="Horsepower")
        .interactive()
    )
    return chart.to_html()


# histogram of counts annual published counts
@app.callback(
    Output("count", "srcDoc"),
    Input("category-widget", "value"),
    Input("mechanics-widget", "value")
    # add for publisher widget
    # ,Input('publisher-widget', 'value')
)
def plot_altair(xcol, ycol):
    chart = (
        alt.Chart(cars)
        .mark_bar()
        .encode(x=xcol, y=ycol, tooltip="Horsepower")
        .interactive()
    )
    return chart.to_html()


@app.callback(
    Output("bar1", "srcDoc"),
    Input("category-widget", "value"),
    Input("mechanics-widget", "value")
    # add for publisher widget
    # ,Input('publisher-widget', 'value')
)
def plot_altair(xcol, ycol):
    chart = (
        alt.Chart(cars)
        .mark_bar()
        .encode(x=xcol, y=ycol, tooltip="Horsepower")
        .interactive()
    )
    return chart.to_html()


@app.callback(
    Output("bar2", "srcDoc"),
    Input("category-widget", "value"),
    Input("mechanics-widget", "value")
    # add for publisher widget
    # ,Input('publisher-widget', 'value')
)
def plot_altair(xcol, ycol):
    chart = (
        alt.Chart(cars)
        .mark_bar()
        .encode(x=xcol, y=ycol, tooltip="Horsepower")
        .interactive()
    )
    return chart.to_html()


@app.callback(
    Output("bar3", "srcDoc"),
    Input("category-widget", "value"),
    Input("mechanics-widget", "value")
    # add for publisher widget
    # ,Input('publisher-widget', 'value')
)
def plot_altair(xcol, ycol):
    chart = (
        alt.Chart(cars)
        .mark_bar()
        .encode(x=xcol, y=ycol, tooltip="Horsepower")
        .interactive()
    )
    return chart.to_html()


@app.callback(
    Output("bar4", "srcDoc"),
    Input("category-widget", "value"),
    Input("mechanics-widget", "value")
    # add for publisher widget
    # ,Input('publisher-widget', 'value')
)
def plot_altair(xcol, ycol):
    chart = (
        alt.Chart(cars)
        .mark_bar()
        .encode(x=xcol, y=ycol, tooltip="Horsepower")
        .interactive()
    )
    return chart.to_html()


@app.callback(
    Output("bar5", "srcDoc"),
    Input("category-widget", "value"),
    Input("mechanics-widget", "value")
    # add for publisher widget
    # ,Input('publisher-widget', 'value')
)
def plot_altair(xcol, ycol):
    chart = (
        alt.Chart(cars)
        .mark_bar()
        .encode(x=xcol, y=ycol, tooltip="Horsepower")
        .interactive()
    )
    return chart.to_html()


@app.callback(
    Output("bar6", "srcDoc"),
    Input("category-widget", "value"),
    Input("mechanics-widget", "value")
    # add for publisher widget
    # ,Input('publisher-widget', 'value')
)
def plot_altair(xcol, ycol):
    chart = (
        alt.Chart(cars)
        .mark_bar()
        .encode(x=xcol, y=ycol, tooltip="Horsepower")
        .interactive()
    )
    return chart.to_html()


if __name__ == "__main__":
    app.run_server(debug=True, host="127.0.0.1", port=8050)
