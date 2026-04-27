from sklearn.ensemble import RandomForestClassifier

def train_model(data):
    data['Future_Close'] = data['Close'].shift(-1)
    data['Target'] = (data['Future_Close'] > data['Close']).astype(int)

    data = data.dropna().copy()

    # 🔥 Correct indentation
    if len(data) < 30:
        print("Warning: Low data, but continuing...")

    X = data[['RSI','EMA20','EMA50','MACD']]
    y = data['Target']

    model = RandomForestClassifier()
    model.fit(X, y)

    return model