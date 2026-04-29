from kiteconnect import KiteConnect
import streamlit as st

API_KEY = st.secrets["API_KEY"]
ACCESS_TOKEN = st.secrets["ACCESS_TOKEN"]

kite = KiteConnect(api_key=API_KEY)
kite.set_access_token(ACCESS_TOKEN)


def place_order_with_sl(symbol, signal, quantity, price, stop_loss_percent):
    try:
        tradingsymbol = symbol.replace(".NS", "")

        # ===== CALCULATE SL PRICE =====
        if signal == "BUY":
            sl_price = price * (1 - stop_loss_percent / 100)
            transaction_type = kite.TRANSACTION_TYPE_BUY
            sl_transaction = kite.TRANSACTION_TYPE_SELL
        elif signal == "SELL":
            sl_price = price * (1 + stop_loss_percent / 100)
            transaction_type = kite.TRANSACTION_TYPE_SELL
            sl_transaction = kite.TRANSACTION_TYPE_BUY
        else:
            return "No valid signal"

        # ===== 1️⃣ PLACE ENTRY ORDER =====
        order_id = kite.place_order(
            variety=kite.VARIETY_REGULAR,
            exchange=kite.EXCHANGE_NSE,
            tradingsymbol=tradingsymbol,
            transaction_type=transaction_type,
            quantity=int(quantity),
            product=kite.PRODUCT_MIS,
            order_type=kite.ORDER_TYPE_MARKET
        )

        # ===== 2️⃣ PLACE STOP LOSS ORDER (SL-M) =====
        kite.place_order(
            variety=kite.VARIETY_REGULAR,
            exchange=kite.EXCHANGE_NSE,
            tradingsymbol=tradingsymbol,
            transaction_type=sl_transaction,
            quantity=int(quantity),
            product=kite.PRODUCT_MIS,
            order_type=kite.ORDER_TYPE_SLM,
            trigger_price=round(sl_price, 1)
        )

        return f"✅ Order + SL placed | Entry ID: {order_id} | SL: ₹{sl_price:.2f}"

    except Exception as e:
        return f"❌ ERROR: {str(e)}"
