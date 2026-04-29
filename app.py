from execution import place_order

# ===== AUTO TRADE TOGGLE =====
auto_trade = st.sidebar.checkbox("🤖 Auto Trade")

if auto_trade:
    st.warning("⚠️ Auto Trading Enabled")

    if signal in ["BUY", "SELL"]:
        result = place_order(symbol, signal, qty)
        st.success(result)
