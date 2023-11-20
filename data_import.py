import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima_model import ARIMA
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
