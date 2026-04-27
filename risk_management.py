# ===============================
# 📊 RISK MANAGEMENT MODULE
# ===============================

def position_size(capital, risk_per_trade, price, stop_loss_pct=0.02):
    """
    Calculate position size based on risk management

    capital: total capital (e.g., 100000)
    risk_per_trade: risk % per trade (e.g., 0.02 = 2%)
    price: current stock price
    stop_loss_pct: stop loss % (default 2%)

    Returns: quantity to trade
    """

    if price <= 0:
        return 0

    risk_amount = capital * risk_per_trade
    stop_loss_amount = price * stop_loss_pct

    size = risk_amount / stop_loss_amount

    return round(size, 2)


def calculate_stop_loss(price, signal, stop_loss_pct=0.02):
    """
    Calculate stop loss price

    BUY  → below price
    SELL → above price
    """

    if price <= 0:
        return None

    if signal == "BUY":
        return round(price * (1 - stop_loss_pct), 2)

    elif signal == "SELL":
        return round(price * (1 + stop_loss_pct), 2)

    return None


def risk_reward_ratio(entry_price, stop_loss, target):
    """
    Calculate Risk:Reward ratio
    """

    if entry_price == stop_loss:
        return None

    risk = abs(entry_price - stop_loss)
    reward = abs(target - entry_price)

    if risk == 0:
        return None

    return round(reward / risk, 2)
