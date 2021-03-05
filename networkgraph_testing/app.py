import dash
import dash_cytoscape as cyto
import dash_html_components as html
import json
import plotly.express as px


# Read in global data

with open("startup_elms.json", "r") as f:
    startup_elms = json.load(f)

startup_elm_list = startup_elms["elm_list"]

col_swatch = px.colors.qualitative.Dark24
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
        cyto.Cytoscape(
            id="core_19_cytoscape",
            layout={"name": "preset"},
            style={"width": "100%", "height": "400px"},
            elements=startup_elm_list,
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)