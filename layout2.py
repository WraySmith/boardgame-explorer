import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import altair as alt
from vega_datasets import data
import dash_bootstrap_components as dbc

# read in dummy data for layout
cars = data.cars()
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# layout components


# left most

def title():
    return html.Div(children=[html.H2("Boardgames Dashboard")])


def description_card():
    """
    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card",
        children=[
            
            html.H4("Welcome to our Boardgames Dashboard"),
            html.Div(
                id="intro",
                children="Explore ..................................",
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
            html.P("Select a Category"),
            dcc.Dropdown(
                id='category-widget',
                value='Horsepower',  
                options=[{'label': col, 'value': col} for col in cars.columns],multi=True),
            html.Br(),
            html.P("Select Mechanics" ),
            dcc.Dropdown(
                id='mechanics-widget',
                value='Displacement',  
                options=[{'label': col, 'value': col} for col in cars.columns]),
            html.Br(),
            html.Br(),
            html.P("Select Pulishers"),
            dcc.Dropdown(
                id='publisher-widget',
                value='Displacement',  
                options=[{'label': col, 'value': col} for col in cars.columns]),
            html.Br(),
            html.Div(
                id="reset-btn-outer",
                children=html.Button(id="reset-btn", children="Reset", n_clicks=0),
            ),
        ])



def lower_description():
     return html.Div(children=[html.H5("This is how the user withh interact with this section")])

# graphs





# layout
app.layout = dbc.Container([# top column

dbc.Row([ dbc.Col([
html.Div(id="top-row",
            className="four columns",
            children=[title()])], width=16)]),

       dbc.Row([ dbc.Col([html.Div(
            id="left-column",
            className="four columns",
            children=[description_card(), generate_control_card()]
            
        )], width=3),
        dbc.Col([
        
        html.Div([
        
             html.H4('Title'), html.P('Description for user interaction'),
            html.Iframe(
                id='scatter',
                style={'border-width': '0', 'width': '100%', 'height': '200px'}),
                html.Iframe(
                    # will be the counts graph
                id='count',
                style={'border-width': '0', 'width': '100%', 'height': '200px'}),
        

])], width=6)]),
dbc.Row([dbc.Col([html.Div(id="bottom left row",
            className="four columns",
            children=[lower_description()])


], width=3), 

])



])
        
        
        


# Set up callbacks/backend
# will be the scatteplot of average game ratings
@app.callback(
    
    Output('scatter', 'srcDoc'),
    Input('category-widget', 'value'),
    Input('mechanics-widget', 'value')
    # add for publisher widget
    #,Input('publisher-widget', 'value')
    )
def plot_altair(xcol, ycol):
    chart = alt.Chart(cars).mark_point().encode(
        x=xcol,
        y=ycol,
        tooltip='Horsepower').interactive()
    return chart.to_html()

# histogram of counts annual published counts 
@app.callback(
    Output('count', 'srcDoc'),
    Input('category-widget', 'value'),
    Input('mechanics-widget', 'value')
    # add for publisher widget
    #,Input('publisher-widget', 'value')
    )
def plot_altair(xcol, ycol):
    chart = alt.Chart(cars).mark_bar().encode(
        x=xcol,
        y=ycol,
        tooltip='Horsepower').interactive()
    return chart.to_html()

#run
if __name__ == '__main__':
    app.run_server(debug=True, host = '127.0.0.1',port=8051)