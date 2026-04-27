import yfinance as yf
import pandas as pd

def get_data(symbol):
    data = yf.download(symbol, period="2y", interval="1d")

    # Remove multi-index
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    return data