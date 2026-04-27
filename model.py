def train_model(data):
    import numpy as np
    from sklearn.ensemble import RandomForestClassifier

    # ✅ Remove NaN safely
    data = data.dropna()

    # ❌ If data too small → skip model
    if len(data) < 20:
        raise ValueError("Not enough data to train model")

    # ✅ Features
    X = data[['RSI', 'MACD']]

    # ✅ Target (simple logic)
    y = (data['Close'].shift(-1) > data['Close']).astype(int)

    # Remove last row (NaN target)
    X = X[:-1]
    y = y[:-1]

    # ❌ Final safety check
    if len(X) == 0:
        raise ValueError("No training data available")

    model = RandomForestClassifier()
    model.fit(X, y)

    return model
