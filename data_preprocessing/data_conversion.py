from data_preprocessing import data_fetching as data
import numpy as np
import pandas as pd
df_yahoo = data.df_yahoo


df = df_yahoo.loc[:, ['Adj Close']]
df.rename(columns=('Adj Close','adj_close'), inplace=True)
print(df.head())