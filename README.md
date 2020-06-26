# [EMP: Earthquake Magnitude Predictor](https://earthquake-magnitude-predictor.herokuapp.com/)

EMP uses machine learning, along with USGS earthquake data, to attempt to predict the magnitude of an earthquake at a specific location. 

## Getting Started

### Prerequisites

- [Git](https://git-scm.com/)
- [Mapbox API Token](https://www.mapbox.com/)
- [Python 3.8](https://www.python.org/)
- [Pipenv](https://pypi.org/project/pipenv/)

### Installing Locally

To start, make sure you have Python 3.8 installed:

```sh
python --version
```

 Next, clone the repository to your local machine:

 ```sh
git clone https://github.com/cdevoogd/EMP.git
 ```

Install the project's requirements (I recommend using pipenv):

```sh
pip install pipenv
pipenv install 
```
Before you can run the project, you will need to set and environment variable with a Mapbox API token. Create a `.env` file in the root directory (i.e. the one with the run.bat and run.sh files) and add your Mapbox token there. Your `.env` file should look like this:

```sh
MAPBOX_ACCESS_TOKEN=pk.1234567890abcdefg
```

Now you should be able to run a development version of the project:
```sh
# We want to run inside of the pipenv virtual environment
pipenv shell
# Depending on your OS you can either use run.bat or run.sh
.\run.bat 
```

## Built With

- [Plotly Dash](https://plotly.com/dash/)
- [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly Graphing Libraries](https://plotly.com/python/)
- [Scikit-Learn](https://scikit-learn.org/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Screenshots

![](https://i.imgur.com/7oXjTyg.png)