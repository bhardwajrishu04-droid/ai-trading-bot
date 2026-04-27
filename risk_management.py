def position_size(capital, risk_per_trade, price):
    risk_amount = capital * risk_per_trade
    size = risk_amount / price
    return round(size, 2)
    return capital * risk
