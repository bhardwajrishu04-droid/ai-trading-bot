import streamlit as st
import time

from data_engine import get_data
from indicators import add_indicators
from model import train_model
from strategy import get_signal
from risk_management import position_size
from execution import place_order_with_sl

# ===== UI =====
st.title("🤖 AI Trading Bot")

# ===== SIDEBAR =====
st.sidebar.title("⚙️ Settings")

auto_refresh = st.sidebar.checkbox("🔄 Live Mode")
auto_trade = st.sidebar.checkbox("🤖 Auto Trade")

refresh_interval = st.sidebar.slider(
    "⏱ Refresh Interval (seconds)",
    min_value=10,
    max_value=60,
    value=15
)

# 🛑 Stop Loss %
stop_loss_percent = st.sidebar.slider(
    "🛑 Stop Loss (%)",
    min_value=0.5,
    max_value=5.0,
    value=1.5
)

# ===== CONFIG =====
symbol = "RELIANCE.NS"
capital = 100000
risk_per_trade = 0.02

# ===== DATA =====
df = get_data(symbol)
df = add_indicators(df)

# ===== MODEL =====
model = train_model(df)

# ===== SIGNAL =====
signal = get_signal(model, df)

# ===== POSITION SIZE =====
price = df["Close"].iloc[-1]
qty = position_size(capital, risk_per_trade, price)

# ===== STOP LOSS CALC =====
if signal == "BUY":
    stop_loss_price = price * (1 - stop_loss_percent / 100)
elif signal == "SELL":
    stop_loss_price = price * (1 + stop_loss_percent / 100)
else:
    stop_loss_price = None

# ===== DISPLAY =====
st.subheader(symbol)

if signal == "BUY":
    st.success(f"Signal: {signal}")
elif signal == "SELL":
    st.error(f"Signal: {signal}")
else:
    st.warning(f"Signal: {signal}")

st.write(f"💰 Trade Size: {qty}")

if stop_loss_price:
    st.write(f"🛑 Stop Loss: ₹{stop_loss_price:.2f}")

# ===== DUPLICATE TRADE CONTROL =====
if "last_signal" not in st.session_state:
    st.session_state.last_signal = None

# ===== MANUAL TRADE =====
if st.button("🚀 Execute Trade"):
    if signal != st.session_state.last_signal:
        result = place_order(symbol, signal, qty)
        st.success(result)
        st.session_state.last_signal = signal
    else:
        st.warning("⚠️ Same signal already executed")

# ===== AUTO TRADE =====
if auto_trade:
    st.warning("⚠️ Auto Trading Enabled")

    if signal in ["BUY", "SELL"] and signal != st.session_state.last_signal:
        result = place_order(symbol, signal, qty)
        st.success(result)
        st.session_state.last_signal = signal

# ===== CHART =====
st.line_chart(df["Close"])

# ===== AUTO REFRESH =====
if auto_refresh:
    time.sleep(refresh_interval)
    st.rerun()
