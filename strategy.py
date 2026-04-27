import numpy as np

def get_signal(model, data):
    latest = data.iloc[-1]

    # ✅ Extract features safely
    features = [
        latest.get('RSI', np.nan),
        latest.get('MACD', np.nan)
    ]

    # ❌ If any value missing → skip prediction
    if any(np.isnan(features)):
        return "HOLD (No valid data)"

    prediction = model.predict([features])[0]

    return "BUY" if prediction == 1 else "SELL"
