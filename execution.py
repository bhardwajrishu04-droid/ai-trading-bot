from kiteconnect import KiteConnect

# ================= LOAD TOKEN =================
with open("access_token.txt", "r") as f:
    ACCESS_TOKEN = f.read().strip()

# ================= API KEY =================
API_KEY = "6c3uhkm1yw56fd8u"

# ================= INIT =================
kite = KiteConnect(api_key=API_KEY)
kite.set_access_token(ACCESS_TOKEN)

# ================= PLACE ORDER FUNCTION =================
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

        else:
            return "No trade"

        return order

    except Exception as e:
        return str(e)
