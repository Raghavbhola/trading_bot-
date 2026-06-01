import time
import hmac
import hashlib
import requests
from bot.logging_config import logger

#BASE_URL = "https://testnet.binancefuture.com"

class BinanceClient:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.session = requests.Session()
        self.session.headers.update({"X-MBX-APIKEY": api_key})

    def _sign(self, params: dict) -> dict:
        params["timestamp"] = int(time.time() * 1000)
        query = "&".join(f"{k}={v}" for k, v in params.items())
        signature = hmac.new(
            self.api_secret.encode(), query.encode(), hashlib.sha256
        ).hexdigest()
        params["signature"] = signature
        return params

    def place_order(self, **kwargs) -> dict:
        params = self._sign(kwargs)
        logger.debug(f"Request params: {kwargs}")
        try:
            resp = self.session.post(f"{BASE_URL}/fapi/v1/order", params=params)
            resp.raise_for_status()
            data = resp.json()
            logger.debug(f"Response: {data}")
            return data
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP error: {e.response.text}")
            raise
        except requests.exceptions.RequestException as e:
            logger.error(f"Network error: {e}")
            raise
