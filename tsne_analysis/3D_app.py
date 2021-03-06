import dash
import pandas as pd

import dash_core_components as dcc
import dash_html_components as html

# from dash.dependencies import Input, Output, State
# import json

# import plotly.express as px
import plotly.graph_objs as go


# Read in global data
tsne_df = pd.read_csv("nodes.csv")

data = []
for idx, val in tsne_df.groupby(tsne_df.highlight):
    if idx == "none":
        continue
    highlight = idx

    scatter = go.Scatter3d(
        name=f"Class {highlight}",
        x=val["x"],
        y=val["y"],
        z=val["z"],
        mode="markers",
        marker=dict(size=val["average_rating"], symbol="circle", opacity=0.5),
    )
    data.append(scatter)

# Layout for the t-SNE graph
tsne_layout = go.Layout(margin=dict(l=0, r=0, b=0, t=0), title=dict(text="test"))

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        # In-browser storage of global variables
        # Main app
        html.Div(
            [
                html.Div(
                    [
                        # The graph
                        dcc.Graph(
                            id="tsne-3d-plot",
                            figure={"data": data, "layout": tsne_layout},
                            style={
                                "height": "80vh",
                            },
                        )
                    ],
                ),
            ],
        ),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
