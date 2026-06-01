# Binance Futures Testnet Trading Bot

A simple Python CLI bot to place Market and Limit orders on Binance Futures Testnet.

## Setup

1. **Clone the repo and install dependencies**
```bash
pip install -r requirements.txt
```

2. **Set your API keys as environment variables**
```bash
# Linux/Mac
export BINANCE_API_KEY=your_api_key_here
export BINANCE_API_SECRET=your_api_secret_here

# Windows
set BINANCE_API_KEY=your_api_key_here
set BINANCE_API_SECRET=your_api_secret_here
```

## How to Run

### Place a MARKET order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a LIMIT order
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 50000
```

## Project Structure
```
trading_bot/
  bot/
    client.py         # Binance API wrapper
    orders.py         # Order placement logic
    validators.py     # Input validation
    logging_config.py # Logger setup
  cli.py              # CLI entry point
  requirements.txt
  README.md
```

## Assumptions
- Uses Binance Futures Testnet only (`https://testnet.binancefuture.com`)
- API keys are passed via environment variables (not hardcoded)
- Logs are saved to `trading_bot.log` in the project root
