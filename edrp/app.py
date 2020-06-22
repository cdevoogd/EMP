import os

import dash
import dash_core_components as dcc
import dash_html_components as html
from dotenv import load_dotenv
import pandas as pd
import plotly.express as px

load_dotenv()

# Load dataset
earthquakes = pd.read_csv('edrp/data/clean_dataset.csv', header=0)

# Create heatmap figure using Scatter Mapbox
px.set_mapbox_access_token(os.getenv('MAPBOX_ACCESS_TOKEN'))
heatmap = px.scatter_mapbox(lat=earthquakes.latitude, lon=earthquakes.longitude)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Earthquake Damage Risk Predictor'),

    html.Div(
        children=[
            dcc.Input(
                id='input_latitude',
                placeholder='38.5816 N'
            ),
            dcc.Input(
                id='input_longitude',
                placeholder='121.4944 W'
            )
        ]
    ),

    dcc.Graph(
        id='local_heatmap',
        figure=heatmap
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)