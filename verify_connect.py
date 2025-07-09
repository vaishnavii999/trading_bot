import os
from binance.client import Client

client = Client(
    os.getenv("BINANCE_API_KEY"),
    os.getenv("BINANCE_API_SECRET"),
    testnet=True
)
client.FUTURES_URL = "https://testnet.binancefuture.com"

print("Server time:", client.futures_time())
