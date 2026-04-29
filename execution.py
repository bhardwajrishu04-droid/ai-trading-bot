from kiteconnect import KiteConnect
import streamlit as st

# ===== LOAD SECRETS =====
API_KEY = st.secrets["API_KEY"]
ACCESS_TOKEN = st.secrets["ACCESS_TOKEN"]

kite = KiteConnect(api_key=API_KEY)
kite.set_access_token(ACCESS_TOKEN)

# ===== ORDER FUNCTION =====
def place_order(symbol, signal, quantity):
    try:
        if signal == "BUY":
            order = kite.place_order(
                variety=kite.VARIETY_REGULAR,
                exchange=kite.EXCHANGE_NSE,
                tradingsymbol=symbol.replace(".NS", ""),
                transaction_type=kite.TRANSACTION_TYPE_BUY,
                quantity=int(quantity),
                product=kite.PRODUCT_MIS,
                order_type=kite.ORDER_TYPE_MARKET
            )
            return f"BUY ORDER PLACED ✅ ID: {order}"

        elif signal == "SELL":
            order = kite.place_order(
                variety=kite.VARIETY_REGULAR,
                exchange=kite.EXCHANGE_NSE,
                tradingsymbol=symbol.replace(".NS", ""),
                transaction_type=kite.TRANSACTION_TYPE_SELL,
                quantity=int(quantity),
                product=kite.PRODUCT_MIS,
                order_type=kite.ORDER_TYPE_MARKET
            )
            return f"SELL ORDER PLACED ✅ ID: {order}"

    except Exception as e:
        return f"ERROR: {e}"
