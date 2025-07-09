import os
from binance.client import Client

client = Client(
    os.getenv("BINANCE_API_KEY"),
    os.getenv("BINANCE_API_SECRET"),
    testnet=True
)
client.FUTURES_URL = "https://testnet.binancefuture.com"

mp = client.futures_mark_price(symbol="BTCUSDT")
# futures_mark_price may return a list or a dict
price = mp[0]["markPrice"] if isinstance(mp, list) else mp["markPrice"]
print("Mark Price:", price)
