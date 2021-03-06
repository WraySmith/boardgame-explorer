import dash
import pandas as pd

# import dash_cytoscape as cyto
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import json
import plotly.express as px
import plotly.graph_objs as go


# Read in global data
tsne_df = pd.read_csv("nodes.csv")

data = []
for idx, val in tsne_df.groupby(tsne_df.highlight):
    highlight = idx

    scatter = go.Scatter3d(
        name=f"Class {highlight}",
        x=val["z"],
        y=val["y"],
        z=val["x"],
        mode="markers",
        marker=dict(size=2.5, symbol="circle"),
    )
    data.append(scatter)

# Layout for the t-SNE graph
tsne_layout = go.Layout(margin=dict(l=0, r=0, b=0, t=0))
# startup_elm_list = startup_elms["elm_list"]

# col_swatch = px.colors.qualitative.Dark24
# def_stylesheet = [
#     {
#         "selector": "." + str(i),
#         "style": {"background-color": col_swatch[i], "line-color": col_swatch[i]},
#     }
#     for i in range(len(network_df["topic_id"].unique()))
# ]
# def_stylesheet += [
#     {
#         "selector": "node",
#         "style": {"width": "data(node_size)", "height": "data(node_size)"},
#     },
#     {"selector": "edge", "style": {"width": 1, "curve-style": "bezier"}},
# ]

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        # In-browser storage of global variables
        # Main app
        html.Div(
            [
                html.H2(
                    "t-SNE Explorer",
                    id="title",
                    style={
                        "float": "left",
                        "margin-top": "20px",
                        "margin-bottom": "0",
                        "margin-left": "20px",
                    },
                ),
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