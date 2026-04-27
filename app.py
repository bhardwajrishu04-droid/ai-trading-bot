import streamlit as st
from data_engine import get_data
from indicators import add_indicators
from model import train_model
from strategy import get_signal
from risk_management import position_size

# ================= UI =================
st.title("🤖 AI Trading Bot")

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

# ================= MAIN LOOP =================
for symbol in SYMBOLS:

    st.markdown(f"---")
    st.subheader(f"📊 {symbol}")

    try:
        # Step 1: Load data
        data = load_data(symbol)

        # Step 2: Add indicators
        data = add_indicators(data)

        # Step 3: Train model
        model = train_model(data)

        # Step 4: Generate signal
        signal = get_signal(model, data)

        # Step 5: Position sizing
        price = data['Close'].iloc[-1]
        size = position_size(CAPITAL, RISK_PER_TRADE, price)

        # ================= UI =================

        # Signal display
        if signal == "BUY":
            st.success(f"Signal: {signal}")
        elif signal == "SELL":
            st.error(f"Signal: {signal}")
        else:
            st.warning(f"Signal: {signal}")

        # Trade size
        st.write(f"💰 Trade Size: {size}")

        # Chart
        st.line_chart(data['Close'])

    except Exception as e:
        st.error(f"{symbol} Error: {e}")
