import pandas as pd
import pandas_datareader as pdr
import datetime as dt
import yfinance as yf

download_source = (r'C:/Users/cwlee2009/Desktop/work/download.xlsx')
yf.pdr_override()

start = dt.datetime(2020, 1, 1)
end = dt.datetime.today()

# df = pdr.get_data_yahoo("005930.KS", start="2021-01-01", end="2022-01-01")
df = pdr.get_data_yahoo("005930.KS", start, end)

print(df.head())

df.to_excel(download_source)
