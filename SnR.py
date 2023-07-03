import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

start_date = '2014-01-01'
end_date = '2018-01-01'
SRC_DATA = 'goog_data.pkl'
yf.pdr_override()


def getData():
    try:
        goog_data = pd.read_pickle(SRC_DATA)
        print("File data found...reading GOOG data")
    except FileNotFoundError:
        print("File not found, downloading GOOG data....")
        goog_data = pdr.get_data_yahoo("GOOG", start=start_date, end=end_date)
        goog_data.to_pickle(SRC_DATA)
    goog_data_signal = pd.DataFrame(index=goog_data.index)
    goog_data_signal['price'] = goog_data['price']
    lows = goog_data['Low']
    highs = goog_data['High']
    return goog_data_signal, lows, highs


def plotGraph():
    fig = plt.figure()
    ax1 = fig.add_subplot(111, ylabel="Google price in $")
    data, highs, lows = getData()
    highs.plot(ax=ax1, color='c', lw=2.)
    lows.plot(ax=ax1, color='y', lw=2.)
    plt.hlines(highs.head(200).max(), lows.index.values[0], lows.index.values[-1], linewidth=2, color='g')
    plt.hlines(lows.head(200).min(), lows.index.values[0], lows.index.values[-1], linewidth=2, color='r')
    plt.axvline(linewidth=2, color='b', x=lows.index.values[200], linestyle=':')
    plt.show()


def main():
    return plotGraph()


def trading_support_resistence(data, bin_width=20):
    # data,_,_ = getData()
    data['sup_tolerance'] = pd.Series(np.zeros(len(data)))
    data['res_tolerance'] = pd.Series(np.zeros(len(data)))
    data['sup_count'] = pd.Series(np.zeros(len(data)))
    data['res_count'] = pd.Series(np.zeros(len(data)))
    data['sup'] = pd.Series(np.zeros(len(data)))
    data['res'] = pd.Series(np.zeros(len(data)))
    data['positions'] = pd.Series(np.zeros(len(data)))
    data['signal'] = pd.Series(np.zeros(len(data)))
    in_support = 0
    in_resistance = 0

    for x in range((bin_width - 1) + bin_width, len(data)):
        data_Section = data[x - bin_width:x + 1]
        support_level = min(data_Section['price'])
        resistance_level = max(data_Section['price'])
        range_level = resistance_level - support_level
        data['res'][x] = resistance_level
        data['sup'][x] = support_level
        data['sup_tolerance'][x] = support_level + 0.2 * range_level
        data['res_tolerance'][x] = resistance_level - 0.2 * range_level

        if data['res_tolerance'][x] <= data['price'][x] <= data['res'][x]:
            in_resistance += 1
            data['res_count'][x] = in_resistance
        elif data['sup_tolerance'][x] >= data['price'][x] >= data['sup'][x]:
            in_support += 1
            data['sup_count'][x] = in_support
        else:
            in_support = in_resistance = 0
        if in_resistance > 2:
            data['signal'][x] = 1
        elif in_support > 2:
            data['signal'][x] = 0

        else:
            data['signal'][x] = data['signal'][x - 1]
    data['positions'] = data['signal'].diff()


data, _, _ = getData()
trading_support_resistence(data=data)


def plotSnR():
    fig= plt.figure()
    ax1= fig.add_subplot(111,ylabel='Google price in $')
