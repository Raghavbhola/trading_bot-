import argparse
import os
from bot.client import BinanceClient
from bot.orders import place_order
from bot.logging_config import logger

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol",     required=True,  help="e.g. BTCUSDT")
    parser.add_argument("--side",       required=True,  choices=["BUY", "SELL"])
    parser.add_argument("--type",       required=True,  choices=["MARKET", "LIMIT"], dest="order_type")
    parser.add_argument("--quantity",   required=True,  type=float)
    parser.add_argument("--price",      required=False, type=float, default=None, help="Required for LIMIT")

    args = parser.parse_args()

    api_key    = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        print("❌ Set BINANCE_API_KEY and BINANCE_API_SECRET environment variables.")
        return

    client = BinanceClient(api_key, api_secret)

    try:
        place_order(
            client,
            symbol     = args.symbol.upper(),
            side       = args.side,
            order_type = args.order_type,
            quantity   = args.quantity,
            price      = args.price,
        )
    except ValueError as e:
        logger.error(f"Validation error: {e}")
        print(f"❌ Validation Error:\n{e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
