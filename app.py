import streamlit as st
from data_engine import get_data
from indicators import add_indicators
from model import train_model
from strategy import get_signal
from risk_management import position_size

# UI Title
st.title("AI Trading Bot")

# Config
SYMBOL = "RELIANCE.NS"
CAPITAL = 100000
RISK_PER_TRADE = 0.02

# Cache data
@st.cache_data
def load_data(symbol):
    return get_data(symbol)

# Main execution
try:
    # Step 1: Load data
    data = load_data(SYMBOL)

    # Step 2: Add indicators
    data = add_indicators(data)

    # Step 3: Train model
    model = train_model(data)

    # Step 4: Generate signal
    signal = get_signal(model, data)

    # Step 5: Position sizing
    size = position_size(
        CAPITAL,
        RISK_PER_TRADE,
        data['Close'].iloc[-1]
    )

    # ================= UI =================

    st.subheader("📊 Signal")
    st.success(signal)

    st.subheader("💰 Trade Size")
    st.write(size)

    st.subheader("📈 Price Chart")
    st.line_chart(data['Close'])

except Exception as e:
    st.error(f"Error: {e}")
    st.stop()
