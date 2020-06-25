"""Dash layout for the application's main dashboard."""

import os

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px

from edrp.app import app
from edrp.data.datasets import earthquakes
import edrp.regressor as regressor

# Defaults are the center of the contiguous US
default_latitude = 39.8283
default_longitude = -98.5795

px.set_mapbox_access_token(os.getenv('MAPBOX_ACCESS_TOKEN'))

scattermap = px.scatter_mapbox(
    center={ 'lat': default_latitude, 'lon': default_longitude },
    color=earthquakes.magnitude,
    data_frame=earthquakes,
    height=500, 
    lat=earthquakes.latitude, 
    lon=earthquakes.longitude,
    # Setting the size & opacity like this allows the larger earthquakes to stand out on the map
    opacity=earthquakes.magnitude / 10,
    size=earthquakes.magnitude ** 5,
    size_max=25,
    zoom=3)

# Shrink the margins (defaults 80) on the top and bottom to 5px
scattermap.update_layout(margin={ 't': 5, 'b': 5 })

layout = html.Div(children=[
    dbc.NavbarSimple(
        brand='Earthquake Damage Risk Predictor',
        color='primary',
        dark=True,
        fluid=True
    ),
    # Top Row - Coordinate Input Form + Prediction
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
            className='d-flex mb-3 justify-content-between',
            style={ 'padding-right': '80px' }
            ),
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
    ),
    dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H5('Prediction:', className='card-title'),
                    html.P(id='magnitude_prediction', className='card-text') 
                ]
            ),
            dbc.CardFooter(id='prediction_confidence')
            
        ]
    )
])


@app.callback(
    [Output('local_scattermap', 'figure'), Output('magnitude_prediction', 'children'), Output('prediction_confidence', 'children')], 
    [Input('submit_coords', 'n_clicks')], 
    [State('input_latitude', 'value'), State('input_longitude', 'value')])
def on_submit_coordinates(n_clicks, latitude, longitude):
    """When coordinates are submitted, this callback calls all of the necessary model & output functions"""
    
    defaults = (scattermap, '', '')
    # This callback will fire when the page loads. So this will return defaults
    if n_clicks is None:
        return defaults

    if not _verify_inputs([latitude, longitude]):
        return defaults

    scattermap.update_layout(mapbox_center={ 'lat': latitude, 'lon': longitude }, mapbox_zoom=6)
    prediction = regressor.predict(latitude, longitude)
    condifence = f'Confidence: {regressor.get_confidence()}'
    
    return scattermap, prediction, condifence

def _verify_inputs(input_list):
    """Checks that each value in the input_list is valid.
    Does not check that the input is a number, as the HTML input wont allow anything other than that to be input
    Returns True if all inputs pass all checks
    """
    for input in input_list:
        if input is None:
            return False
    return True
