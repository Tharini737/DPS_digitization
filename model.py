import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.seasonal import seasonal_decompose


#data cleaning 
raw_data = pd.read_csv("C:\\hmm\\dps\\raw_data.csv", usecols= ['MONATSZAHL', 'AUSPRAEGUNG', 'JAHR', 'MONAT', 'WERT'])
def data_prep(*args):
    df_filtered = raw_data[raw_data['JAHR'] <= 2020]
    df_data = df_filtered.copy()
    df_filtered['MONAT'] = pd.to_datetime(df_filtered['MONAT'],format = '%Y%m')
    df_filtered.rename(columns = {'MONAT':'Time'},inplace = True)
    df_filtered.set_index(df_filtered['Time'],inplace = True)
    df_filtered.drop(columns = ['JAHR','Time'], inplace = True)
    df_filtered.sort_index(inplace = True)
    return df_filtered


#data import
df_filtered = data_prep(raw_data)

def predictions(year, month): 
    forecast_date = f"{year}-{str(month).zfill(2)}-01"

    category_combinations = df_filtered[['MONATSZAHL', 'AUSPRAEGUNG']].drop_duplicates()

# Dictionary to store models
    models = {}
    for _, row in category_combinations.iterrows():
        category = row['MONATSZAHL']
        auspraegung = row['AUSPRAEGUNG']

        # Filter the data for the current combination
        selected_series = df_filtered[(df_filtered['MONATSZAHL'] == category) & (df_filtered['AUSPRAEGUNG'] == auspraegung)]['WERT']
        

        # Check if the series is not empty
        if not selected_series.empty:
            model = SARIMAX(selected_series, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
            results = model.fit()
            models[(category, auspraegung)] = results
    forecast = models[('Alkoholunfälle', 'insgesamt')].get_prediction(start=pd.to_datetime(forecast_date), end=pd.to_datetime(forecast_date))
    forecast_value = forecast.predicted_mean[0]
    return forecast_value
