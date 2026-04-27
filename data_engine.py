import yfinance as yf
import pandas as pd
import time

def get_data(symbol):
    time.sleep(2)  # ✅ prevent rate limit

    data = yf.download(symbol, period="1y", interval="1d", threads=False)

    # ✅ check empty data
    if data.empty:
        raise ValueError("No data fetched. Try again later.")

    # Remove multi-index if exists
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data = data.dropna()

    return data
