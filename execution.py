from kiteconnect import KiteConnect

# Load token
import os

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN", "")

API_KEY = "6c3uhkm1yw56fd8u"

kite = KiteConnect(api_key=API_KEY)
kite.set_access_token(ACCESS_TOKEN)


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

        return order

    except Exception as e:
        print("Order Error:", e)
