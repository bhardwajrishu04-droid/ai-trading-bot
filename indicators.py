import pandas as pd
import ta

def add_indicators(data):
    # 🔥 column names fix
    data.columns = [col.capitalize() for col in data.columns]

    # ✅ check if Close exists
    if "Close" not in data.columns:
        raise Exception(f"Available columns: {data.columns}")

    close = data["Close"]

    # Indicators
    data["RSI"] = ta.momentum.RSIIndicator(close).rsi()
    data["EMA20"] = ta.trend.EMAIndicator(close, window=20).ema_indicator()

    return data
