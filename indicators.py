import ta

def add_indicators(data):
    # 🔥 FORCE 1D SERIES (FINAL FIX)
    close = data['Close']

    data['RSI'] = ta.momentum.RSIIndicator(close=close).rsi()
    data['EMA20'] = ta.trend.EMAIndicator(close=close, window=20).ema_indicator()
    data['EMA50'] = ta.trend.EMAIndicator(close=close, window=50).ema_indicator()
    data['MACD'] = ta.trend.MACD(close=close).macd()

    data = data.dropna().copy()
    return data
