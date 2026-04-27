def get_signal(model, latest):
    prediction = model.predict([[
        latest['RSI'],
        latest['EMA20'],
        latest['EMA50'],
        latest['MACD']
    ]])
    
    return "BUY" if prediction[0] == 1 else "SELL"