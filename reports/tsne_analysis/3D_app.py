import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

# Read in global data
tsne_df = pd.read_csv("nodes.csv")

data = []
for idx, val in tsne_df.groupby(tsne_df.highlight):
    if idx == "none":
        marker_style = dict(
            size=val["average_rating"] * 1.5, symbol="circle", opacity=0.1, color="grey"
        )
    else:
        marker_style = dict(
            size=val["average_rating"] * 1.5, symbol="circle", opacity=0.4
        )

    scatter = go.Scatter3d(
        name=idx,
        x=val["x"],
        y=val["y"],
        z=val["z"],
        mode="markers",
        marker=marker_style,
    )
    data.append(scatter)


# Layout for the t-SNE graph
tsne_layout = go.Layout(margin=dict(l=0, r=0, b=0, t=0), title=dict(text="test"))

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Graph(
            id="tsne-3d-plot",
            figure={"data": data, "layout": tsne_layout},
            style={"height": "80vh"},
        ),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)
