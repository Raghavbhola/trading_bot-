from bot.client import BinanceClient
from bot.validators import validate_inputs
from bot.logging_config import logger

def place_order(client: BinanceClient, symbol, side, order_type, quantity, price=None):
    validate_inputs(symbol, side, order_type, quantity, price)

    params = dict(symbol=symbol, side=side, type=order_type, quantity=quantity)
    if order_type == "LIMIT":
        params.update(price=price, timeInForce="GTC")

    # Print summary
    print("\n--- Order Request ---")
    for k, v in params.items():
        print(f"  {k}: {v}")

    logger.info(f"Placing {order_type} {side} order for {quantity} {symbol}")
    response = client.place_order(**params)

    # Print response
    print("\n--- Order Response ---")
    print(f"  Order ID  : {response.get('orderId')}")
    print(f"  Status    : {response.get('status')}")
    print(f"  Executed  : {response.get('executedQty')}")
    print(f"  Avg Price : {response.get('avgPrice', 'N/A')}")
    print("\n✅ Order placed successfully!\n")

    logger.info(f"Order success | ID={response.get('orderId')} status={response.get('status')}")
    return response
