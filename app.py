import streamlit as st
from data_engine import get_data
from indicators import add_indicators
from model import train_model
from strategy import get_signal
from risk_management import position_size
from config import SYMBOL,CAPITAL,RISK_PER_TRADE

st.title("AI Trading Bot")

data = get_data(SYMBOL)
data = add_indicators(data)

model = train_model(data)

latest = data.iloc[-1]
signal = get_signal(model, latest)

size = position_size(CAPITAL, RISK_PER_TRADE)

st.write("Signal:", signal)
st.write("Trade Size:", size)