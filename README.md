# Binance Futures Testnet Trading Bot

A lightweight Python command‑line trading bot for Binance Futures Testnet (USDT‑M).  

## Overview

This project provides a reusable, well‑structured Python client (`BasicBot`) and a CLI (`cli.py`) for:

- **Connecting** to Binance Futures Testnet (`https://testnet.binancefuture.com`)  
- **Loading** API credentials from environment variables  
- **Placing** MARKET, LIMIT, and STOP‑LIMIT orders (both buy & sell)  
- **Listing** open (resting) orders  
- **Canceling** orders by ID  
- **Viewing** recent trade history  
- **Logging** all requests, responses, and errors to `bot.log`

## Quickstart

1. **Clone**  
   ```bash
   git clone https://github.com/vaishnavii999/trading_bot.git
   cd trading_bot
