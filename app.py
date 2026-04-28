import streamlit as st
import time

from data_engine import get_data
from indicators import add_indicators
from model import train_model
from strategy import get_signal
from risk_management import position_size
from execution import place_order   # ✅ IMPORTANT

# ================= UI =================
st.title("🤖 AI Trading Bot")

# ================= SIDEBAR =================
st.sidebar.title("⚙️ Settings")

auto_refresh = st.sidebar.checkbox("🔄 Live Mode")
refresh_interval = st.sidebar.slider(
    "⏱ Refresh Interval (seconds)",
    min_value=10,
    max_value=60,
    value=15
)

# 🔥 AUTO TRADE BUTTON
AUTO_TRADE = st.sidebar.checkbox("🚀 Enable Auto Trading")

# ================= CONFIG =================
SYMBOLS = [
    "RELIANCE.NS",
    "TCS.NS",
    "INFY.NS",
    "HDFCBANK.NS",
    "ICICIBANK.NS"
]

CAPITAL = 100000
RISK_PER_TRADE = 0.02

# ================= CACHE =================
@st.cache_data
def load_data(symbol):
    return get_data(symbol)

# ================= MAIN =================
for symbol in SYMBOLS:

    st.markdown("---")
    st.subheader(f"📊 {symbol}")

    try:
        # Step 1: Data
        data = load_data(symbol)

        if data is None or data.empty:
            st.error("❌ No data found")
            continue

        # Step 2: Indicators
        data = add_indicators(data)

        # Step 3: Model
        model = train_model(data)

        # Step 4: Signal
        signal = get_signal(model, data)

        # Step 5: Position Size
        price = data['Close'].iloc[-1]
        size = position_size(CAPITAL, RISK_PER_TRADE, price)

        # ================= UI =================

        # Signal Display
        if signal == "BUY":
            st.success(f"Signal: {signal}")
        elif signal == "SELL":
            st.error(f"Signal: {signal}")
        else:
            st.warning(f"Signal: {signal}")

        st.write(f"💰 Trade Size: {size}")

        # 🔒 SAFETY CHECK
        if size < 1:
            st.warning("⚠️ Size too small, skipping trade")
            continue

        # 🔥 AUTO TRADE EXECUTION
        if AUTO_TRADE:
            st.warning("🚀 AUTO TRADE ACTIVE")

            order = place_order(symbol, signal, size)

            st.write("📦 Order Result:", order)

        # Chart
        st.line_chart(data['Close'])

    except Exception as e:
        st.error(f"{symbol} Error: {e}")

# ================= AUTO REFRESH =================
if auto_refresh:
    time.sleep(refresh_interval)
    st.rerun()
