import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import altair as alt
from vega_datasets import data
import dash_bootstrap_components as dbc

# read in dummy data for layout
cars = data.cars()

# Setup app and layout/frontend
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([
    html.H1('Boardgames Dashboard'),
    dbc.Row([
        dbc.Col([
            # will be Category
            dcc.Dropdown(
                id='category-widget',
                value='Horsepower',  
                options=[{'label': col, 'value': col} for col in cars.columns],multi=True),
                # will be Mechanics
            dcc.Dropdown(
                id='mechanics-widget',
                value='Displacement',  
                options=[{'label': col, 'value': col} for col in cars.columns]),
                dcc.Dropdown(
                id='publisher-widget',
                value='Displacement',  
                options=[{'label': col, 'value': col} for col in cars.columns])
                ],
            md=4),
        dbc.Col([ html.H4('Title'), html.P('Description for user interaction'),
            html.Iframe(
                id='scatter',
                style={'border-width': '0', 'width': '100%', 'height': '400px'}),
                html.Iframe(
                    # will be the counts graph
                id='count',
                style={'border-width': '0', 'width': '100%', 'height': '400px'})
])]),
dbc.Row([ 
    dbc.Col([ html.H4('Description'),html.P('Description paragraph')]), 
    



 dbc.Col([ html.H4('Top Ranked Games'),

html.Iframe(
                id='bar1',
                style={'border-width': '0', 'width': '100%', 'height': '400px'}),
                html.Iframe(
                id='bar4',
                style={'border-width': '0', 'width': '100%', 'height': '400px'})])

, dbc.Col([ html.Iframe(
                id='bar2',
                style={'border-width': '0', 'width': '100%', 'height': '400px'}),
                html.Iframe(
                id='bar5',
                style={'border-width': '0', 'width': '100%', 'height': '400px'})]),
                dbc.Col([
                html.Iframe(
                id='bar3',
                style={'border-width': '0', 'width': '100%', 'height': '400px'}),
                html.Iframe(
                id='bar6',
                style={'border-width': '0', 'width': '100%', 'height': '400px'})])]),
                
                
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

@app.callback(
    
    Output('bar1', 'srcDoc'),
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
@app.callback(
    
    Output('bar2', 'srcDoc'),
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
@app.callback(
    
    Output('bar3', 'srcDoc'),
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
@app.callback(
    
    Output('bar4', 'srcDoc'),
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
@app.callback(
    
    Output('bar5', 'srcDoc'),
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
@app.callback(
    
    Output('bar6', 'srcDoc'),
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

if __name__ == '__main__':
    app.run_server(debug=True, host = '127.0.0.1',port=8050)