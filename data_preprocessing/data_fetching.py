from __future__ import print_function
import pandas as pd
import datetime as dt
import pandas_datareader.data as web
import os
import yfinance as yf
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException


start = dt.datetime(2014, 1,1)
end = dt.datetime.today()
# import data from yahoo finance using yfinance
df_yahoo = yf.download('AAPL', start=start, end=end, progress=False)
print("Yahoo: \n", df_yahoo.tail())

# importing data from alpha-vantage using pandas_datareader

df_av = web.DataReader('AAPL', 'av-daily', start=start, end=end, api_key=os.getenv('ALPHAVANTAGE_API_KEY'))
print('Alphavantage: \n',df_av.tail())

# importing data from quandl using pandas-datareader
df_quandl = web.DataReader('AAPL.US', 'quandl', start=start, end=end, api_key=os.getenv('QUANDL_API_KEY'))
print('Quandl: \n', df_quandl.tail())

# importing data from intrinio using intrinio sdk


intrinio.ApiClient().set_api_key('OmE1MzBmZjA2ODA0MjY5MzZjNmFmMmYyNzUzNDI0MzM5')
intrinio.ApiClient().allow_retries(True)

identifier = "AAPL"
start_date = "2018-01-01"
end_date = "2019-01-01"
frequency = 'daily'
page_size = 100
next_page = "~null"

response = intrinio.SecurityApi().get_security_stock_prices(identifier, start_date=start_date, end_date=end_date, frequency=frequency, page_size=page_size, next_page=next_page)
print(response)
    
