import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import altair as alt
from vega_datasets import data
import dash_bootstrap_components as dbc
from vega_datasets import data
import pandas as pd
import sys

from functions import *



# read in data
data = pd.read_csv('board_game.csv')



app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


#subsetting categories

category_ratings_df = data.copy()
category_ratings_df['category'] = category_ratings_df['category'].str.split(",")
category_ratings_df = category_ratings_df.explode('category')
list_categories=list(category_ratings_df.category.unique())

list_cat=['Economic', 'Political','Ancient']


#subsetting mechanics

mechanic_ratings_df = data.copy()
mechanic_ratings_df['mechanic'] = mechanic_ratings_df['mechanic'].str.split(",")
mechanic_df = mechanic_ratings_df.explode('mechanic')

list_mechanics=list(mechanic_df.mechanic.unique())

list_mech=['Area Control', 'Risk-taking']

#subsetting publishers

publisher_ratings_df = data.copy()
publisher_ratings_df['publisher'] = publisher_ratings_df['publisher'].str.split(",")
publisher_df = publisher_ratings_df.explode('publisher')

list_publisher=list(publisher_df.publisher.unique())

list_pub=['3M', 'KOSMOS']

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
                value='Economic',  
                options=[{'label': name, 'value': name} for name in list_cat]),
            html.Br(),
            html.P("Select Mechanics" ),
            dcc.Dropdown(
                id='mechanics-widget',
                value='Trick-taking',  
                options=[{'label': name, 'value': name} for name in list_mech]),
            html.Br(),
            html.Br(),
            html.P("Select Pulishers"),
            dcc.Dropdown(
                id='publisher-widget',
                value='3M',  
                options=[{'label': name, 'value': name} for name in list_pub]),
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
    Input('publisher-widget', 'value'),
    Input('mechanics-widget', 'value')
    
    )
def call_scatter(c,m,p):
    chart=scatter_plot_dates(cat=c,mech=m,pub=p)
    return chart.to_html()

# histogram of counts annual published counts 
@app.callback(
    Output('count', 'srcDoc'),
    Input('category-widget', 'value'),
    Input('publisher-widget', 'value'),
    Input('mechanics-widget', 'value')
    
    )
def call_counts(c,m,p):
    chart2=count_plot_dates(cat=c,mech=m,pub=p)
    return chart2.to_html()

#run
if __name__ == '__main__':
    app.run_server(debug=True, host = '127.0.0.1',port=8051)