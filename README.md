# DPS_digitization
forecasting accidents

## Project Overview

Forecasting Accidents is a DPS challenge project focused on predicting future accidents using time series data. The project utilizes historical data containing attributes such as year, month, category (MONATSZAHL), and type of accident (AUSPRAEGUNG) to build predictive models. These models aim to assist in understanding accident trends and preparing more effectively for future scenarios.

## Features
- Visualization of trends, seasons, and residuals
- Time series forecasting using SARIMAX model.
- Analysis of accident data based on three categories Verkehrsunfälle, Fluchtunfälle, Alkoholunfälle and types including insgesamt,     Verletzte und Getötete, mit Personenschäden.
- Monthly and yearly trend analysis.


##
- API Endpoint http://127.0.0.1:8000/predictions provides the predicted number of accidents value. 
- A POST request to the URL with a dictionary containing year (int), month(int), category(str) and accident_type(str) shows the predicted number of accidents.


## Installation

Before running the project, ensure you have Python installed on your system. You can then set up the project environment with the following steps:

```bash
git clone https://github.com/Tharini737/DPS_digitization.git 
cd DPS_digitization 
