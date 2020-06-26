import dash
from dotenv import load_dotenv

load_dotenv()

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=['https://stackpath.bootstrapcdn.com/bootswatch/4.5.0/flatly/bootstrap.min.css'])
app.title = 'Earthquake Magnitude Predictor'
server = app.server
