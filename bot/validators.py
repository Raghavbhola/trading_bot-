def validate_inputs(symbol, side, order_type, quantity, price):
    errors = []

    if not symbol.isalpha() or len(symbol) < 3:
        errors.append("Invalid symbol. Example: BTCUSDT")

    if side not in ("BUY", "SELL"):
        errors.append("Side must be BUY or SELL")

    if order_type not in ("MARKET", "LIMIT"):
        errors.append("Order type must be MARKET or LIMIT")

    if quantity <= 0:
        errors.append("Quantity must be greater than 0")

    if order_type == "LIMIT" and (price is None or price <= 0):
        errors.append("Price is required for LIMIT orders and must be > 0")

    if errors:
        raise ValueError("\n".join(errors))
