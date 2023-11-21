# Forecasting Accidents

## Project Overview

Forecasting Accidents is a DPS challenge project focused on predicting future accidents using time series data. The project utilizes historical data containing attributes such as year, month, category (MONATSZAHL), and type of accident (AUSPRAEGUNG) to build predictive models. These models aim to assist in understanding accident trends and preparing more effectively for future scenarios.

## Features
- Visualization of trends, seasons, and residuals
- Dickey-Fuller test
- Time series forecasting using SARIMAX model.
- Analysis of accident data based on three categories Verkehrsunfälle, Fluchtunfälle, Alkoholunfälle and types including insgesamt,     Verletzte und Getötete, mit Personenschäden.
- Monthly and yearly trend analysis.
- Integration tests to ensure execution of function components


##
- API Endpoint http://127.0.0.1:8000/predictions provides the predicted number of accidents value. 
- A POST request to the URL with a dictionary containing year (int), month(int), category(str) and accident_type(str) shows the predicted number of accidents.
- Tested the API endpoint and its predictions for the POST requests using POSTMAN 

## Structure of the project

dps_accident_forecast/
│
├── model/                        # Model directory for prediction logic and data analysis
│   ├── __init__.py               # Makes 'model' a Python package
│   ├── prediction.py             # Contains the prediction logic
│   └── visualization.ipynb       # Jupyter notebook for data visualization
│
├── api/                          # API directory for FastAPI endpoints
│   ├── __init__.py               # Makes 'api' a Python package
│   └── endpoints.py              # Contains FastAPI endpoints for the application
│
├── tests/                        # Tests directory for unit and integration tests
│   ├── __init__.py               # Makes 'tests' a Python package
│   └── test.py                   # Contains test cases for the application
│
├── data/                         # Data directory for storing datasets
│   └── raw_data.csv              # Raw data file containing time series data used in the project
│
├── requirements.txt              # File containing a list of dependencies for the project



## Installation

Before running the project, ensure you have Python installed on your system. You can then set up the project environment with the following steps:

```bash
git clone https://github.com/Tharini737/DPS_digitization.git 
cd DPS_digitization 
pip install -r requirements.txt


