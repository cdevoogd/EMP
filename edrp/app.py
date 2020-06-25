import os

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dotenv import load_dotenv
import pandas as pd
import plotly.express as px

load_dotenv()

earthquakes = pd.read_csv('edrp/data/clean_dataset.csv', header=0)
px.set_mapbox_access_token(os.getenv('MAPBOX_ACCESS_TOKEN'))

# Defaults are the center of the contiguous US
default_latitude = 39.8283
default_longitude = -98.5795

# Generate the default map
scattermap = px.scatter_mapbox(
    center={ 'lat': default_latitude, 'lon': default_longitude },
    color=earthquakes.magnitude,
    data_frame=earthquakes,
    height=750, 
    lat=earthquakes.latitude, 
    lon=earthquakes.longitude,
    # Setting the size & opacity like this allows the larger earthquakes to stand out on the map
    opacity=earthquakes.magnitude / 10,
    size=earthquakes.magnitude ** 5,
    size_max=25,
    zoom=3)

# Shrink the margins (defaults 80) on the top and bottom to 5px
scattermap.update_layout(margin={ 't': 5, 'b': 5 })

stylesheets = ['https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/flatly/bootstrap.min.css']
app = dash.Dash(__name__, external_stylesheets=stylesheets)
app.layout = html.Div(children=[
    dbc.NavbarSimple(
        brand='Earthquake Damage Risk Predictor',
        color='primary',
        dark=True,
        fluid=True
    ),

    dbc.Row(
        [
            dbc.Col(
                dbc.FormGroup(
                    [
                        dbc.Label('Latitude', html_for='input_latitude'),
                        dbc.Input(
                            className='input_latitude',
                            id='input_latitude', 
                            type='number', 
                            placeholder=default_latitude
                        )
                    ],
                    className='mr-1 mt-3'
                ),
                style={ 'max-width': '20%' }
            ),
            dbc.Col(
                dbc.FormGroup(
                    [
                        dbc.Label('Longitude', html_for='input_longitude'),
                        dbc.Input(
                            className='input_longitude',
                            id='input_longitude',
                            type='number',
                            placeholder=default_longitude
                        )
                    ],
                    className='mr-1 mt-3'
                ),
                style={ 'max-width': '20%' }
            ),
            dbc.Col(
                dbc.Button(
                    'Submit', 
                    id='submit_coords', 
                    color='primary',
                    className='align-self-end'
                ),
                # Setting this column to flex allows the submit button to line up with the bottom
                # by using 'align-self-end'
                className='d-flex mb-3'
            )
        ],
        form=True,
        style={ 'padding-left': '80px' }
    ),
    

    dcc.Graph(
        id='local_scattermap',
        figure=scattermap,
        config={
            'displayModeBar': False
        }
    )
])

@app.callback(Output('local_scattermap', 'figure'), [Input('submit_coords', 'n_clicks')], [State('input_latitude', 'value'), State('input_longitude', 'value')])
def update_map_target(n_clicks, latitude, longitude):
    # This callback will fire when the page loads. We don't want to update the map until the button is actually clicked
    if n_clicks is not None:
        scattermap.update_layout(mapbox_center={ 'lat': latitude, 'lon': longitude }, mapbox_zoom=6)
    return scattermap

if __name__ == '__main__':
    app.run_server(debug=True)