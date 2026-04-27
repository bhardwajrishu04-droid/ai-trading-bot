import streamlit as st
from data_engine import get_data
from indicators import add_indicators
from model import train_model
from strategy import get_signal
from risk_management import position_size

# UI Title
st.title("AI Trading Bot")

SYMBOL = "RELIANCE.NS"
CAPITAL = 100000
RISK_PER_TRADE = 0.02

# ✅ Cache data
@st.cache_data
def load_data(symbol):
    return get_data(symbol)

# ✅ Safe execution
try:
    data = load_data(SYMBOL)
    data = add_indicators(data)

except Exception as e:
    st.error(f"Error: {e}")
    st.stop()

# ✅ Show chart
st.subheader("Price Chart")
st.line_chart(data['Close'])

# ✅ Add indicators
data = add_indicators(data)

# ✅ Train model
model = train_model(data)

# ✅ Get signal
signal = get_signal(model, data)

# ✅ Position sizing
size = position_size(CAPITAL, RISK_PER_TRADE)

# ✅ Display output
st.subheader("Trade Signal")
st.write("Signal:", signal)
st.write("Trade Size:", size)

# ✅ Latest price
st.write("Current Price:", data['Close'].iloc[-1])
