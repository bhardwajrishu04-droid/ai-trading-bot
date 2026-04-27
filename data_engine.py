import yfinance as yf
import pandas as pd
import time

def get_data(symbol):
    try:
        time.sleep(5)  # prevent rate limit

        data = yf.download(
            symbol,
            period="1y",
            interval="1d",
            threads=False
        )

        if data.empty:
            raise ValueError("No data fetched")

        # Fix multi-index if exists
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = data.columns.get_level_values(0)

        data = data.dropna()

        return data

    except Exception as e:
        print(f"Data error: {e}")
        return pd.DataFrame()
