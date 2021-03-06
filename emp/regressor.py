"""The regressor module contains the decision tree used to predict earthquake magnitudes."""
import logging

import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

from emp.data.datasets import earthquakes

logger = logging.getLogger(__name__)

x = earthquakes[['latitude', 'longitude']]
y = earthquakes[['magnitude']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.05, random_state=40)

regressor = DecisionTreeRegressor().fit(x_train, y_train)

def predict(latitude, longitude):
    prediction = regressor.predict([[latitude, longitude]])
    logger.info(f'Regressor generated the following predicition for ({latitude}, {longitude}): {prediction}')
    return prediction

def get_confidence(digits=2):
    error = mean_squared_error(y_test, regressor.predict(x_test), multioutput='uniform_average')
    score = 1.00 - error
    confidence = round(score, digits)
    logger.info(f'Regressor generated the following confidence: {confidence}')
    return confidence
