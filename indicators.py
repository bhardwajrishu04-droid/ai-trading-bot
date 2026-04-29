import pandas as pd
import ta

def add_indicators(data):
    # Column fix
    data.columns = [col.capitalize() for col in data.columns]

    if "Close" not in data.columns:
        raise Exception(f"Columns found: {data.columns}")

    close = data["Close"]

    # Indicators
    data["RSI"] = ta.momentum.RSIIndicator(close).rsi()
    data["EMA20"] = ta.trend.EMAIndicator(close, window=20).ema_indicator()

    # 🔥 ADD THIS (IMPORTANT)
    macd = ta.trend.MACD(close)
    data["MACD"] = macd.macd()

    # Drop NaN
    data.dropna(inplace=True)

    return data
