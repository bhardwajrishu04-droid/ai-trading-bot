def train_model(data):
    import numpy as np
    from sklearn.ensemble import RandomForestClassifier

    # ✅ Step 1: Remove NaN values
    data = data.dropna().copy()

    # ❌ If not enough rows → stop
    if len(data) < 20:
        raise ValueError("Not enough data to train model")

    # ✅ Step 2: Features
    X = data[['RSI', 'MACD']].copy()

    # ✅ Step 3: Target (next day movement)
    y = (data['Close'].shift(-1) > data['Close']).astype(int)

    # ❌ Remove last row (NaN target)
    X = X[:-1]
    y = y[:-1]

    # ✅ Step 4: Final safety checks
    if X.empty or y.empty:
        raise ValueError("No training data available")

    if len(X) != len(y):
        raise ValueError("Mismatch between X and y")

    # ✅ Step 5: Train model
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42
    )

    model.fit(X, y)

    return model
