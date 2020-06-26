"""The index module routes URL calls and displays the corresponding layout/page.

This module is setup to be easily expandable as new pages are added to the application. To add pages to the website, 
simply import the layout and add the route to the callback function.

For more info & examples, see: https://dash.plotly.com/urls

Note: The index needs to stay seperate from the app module to prevent circular imports.
"""
import logging
# Logging needs to be setup first so that it takes precedence
formatter = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='emp.log', format=formatter, level=logging.INFO)
logger = logging.getLogger(__name__)    

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from emp.app import app, server
from emp.layouts import dashboard

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def set_page_content(pathname):
    if pathname == '/':
        return dashboard.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)