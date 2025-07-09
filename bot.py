import os
import logging
from binance.client import Client

class BasicBot:
    def __init__(self):
        key    = os.getenv("BINANCE_API_KEY")
        secret = os.getenv("BINANCE_API_SECRET")
        self.client = Client(key, secret, testnet=True)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"
        logging.info("Client initialized")

    def place_market_order(self, symbol, side, qty):
        try:
            return self.client.futures_create_order(
                symbol=symbol.upper(),
                side=side.upper(),
                type="MARKET",
                quantity=qty
            )
        except Exception as e:
            logging.error(f"Market order failed: {e}")
            print(f"❌ Market order failed: {e}")
            return None

    def place_limit_order(self, symbol, side, qty, price):
        try:
            return self.client.futures_create_order(
                symbol=symbol.upper(),
                side=side.upper(),
                type="LIMIT",
                timeInForce="GTC",
                quantity=qty,
                price=price
            )
        except Exception as e:
            logging.error(f"Limit order failed: {e}")
            print(f"❌ Limit order failed: {e}")
            return None

    def place_stop_limit(self, symbol, side, qty, stop_price, limit_price):
        """Bonus: Stop-Limit order"""
        try:
            return self.client.futures_create_order(
                symbol=symbol.upper(),
                side=side.upper(),
                type="STOP",
                timeInForce="GTC",
                quantity=qty,
                price=limit_price,
                stopPrice=stop_price
            )
        except Exception as e:
            logging.error(f"Stop-Limit failed: {e}")
            print(f"❌ Stop-Limit failed: {e}")
            return None

    def get_open_orders(self, symbol=None):
        return self.client.futures_get_open_orders(
            symbol=symbol.upper() if symbol else None
        )

    def cancel_order(self, symbol, order_id):
        try:
            return self.client.futures_cancel_order(
                symbol=symbol.upper(),
                orderId=order_id
            )
        except Exception as e:
            logging.error(f"Cancel order failed: {e}")
            print(f"❌ Cancel order failed: {e}")
            return None

    def get_trade_history(self, symbol, limit=10):
        try:
            return self.client.futures_account_trades(
                symbol=symbol.upper(),
                limit=limit
            )
        except Exception as e:
            logging.error(f"Fetch trades failed: {e}")
            print(f"❌ Fetch trades failed: {e}")
            return None
