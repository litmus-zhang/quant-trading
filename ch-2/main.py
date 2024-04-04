import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import os
import yfinance as yf


start = dt.datetime(2014, 1, 1)
end = dt.datetime.today()
SRC_data_file = 'goog_data.pkl'
data = yf.download('GOOG', start=start, end=end, progress=False)
# print(data.tail())

s = web.DataReader('GOOG','quandl', start=start, end=end, api_key='CKNiekivKSX4c4aGvmvi')
print(s.head())


# try: 
#     goog_data2 = pd.read_pickle(SRC_data_file)
# except FileNotFoundError:
#     goog_data2 = web.DataReader('GOOG', 'av-daily', start, end, api_key=os.getenv('ALPHAVANTAGE_API_KEY'))
#     goog_data2.to_pickle(SRC_data_file)

# goog_data = goog_data2.tail(620)
# lows = goog_data('Low')
# highs =  goog_data('High')

# import matplotlib.pyplot as plt

# fig = plt.figure()
# ax1 = fig.add_subplot(111, ylabel= "Google price in $")
# highs.plot(ax=ax1, color='c', lw=2.)
# lows.plot(ax=ax1, color='y', lw=2.)
# plt.hlines(highs.head(200).max(), lows.index.values[0], lows.index.values[-1], linestyles='solid', linewidth=2, colors='g')
# plt.hlines(lows.head(200).min(), lows.index.values[0], lows.index.values[-1], linewidth=2, colors='r')
# plt.axvline(linewidth=2, color='b', x=lows.index.values[200], linestyles=':')
# plt.show()
