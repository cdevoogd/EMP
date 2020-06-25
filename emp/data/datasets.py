"""The datasets module is where the datasets used are loaded into the app and are available for access by other modules."""

import pandas as pd

earthquakes = pd.read_csv('emp/data/earthquakes_clean.csv', header=0)