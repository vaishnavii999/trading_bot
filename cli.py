import argparse, logging
from bot import BasicBot
from logger import setup_logger

def main():
    setup_logger()
    p = argparse.ArgumentParser(
        description="Testnet Futures Bot: trade, open_orders, cancel, trades"
    )
    p.add_argument(
        "--action",
        choices=["trade","open_orders","cancel","trades"],
        default="trade",
        help="Action to perform"
    )
    p.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    p.add_argument("--side", choices=["BUY","SELL"], help="For trade")
    p.add_argument(
        "--type",
        choices=["MARKET","LIMIT","STOP"],
        help="Order type: MARKET, LIMIT, or STOP"
    )
    p.add_argument("--qty", type=float, help="Quantity for trade")
    p.add_argument("--price", type=float, help="Limit price (for LIMIT/STOP)")
    p.add_argument("--stop_price", type=float, help="Stop trigger (for STOP)")
    p.add_argument("--order_id", type=int, help="For cancel")
    p.add_argument("--limit", type=int, default=10, help="For trades history")

    args = p.parse_args()
    bot = BasicBot()

    if args.action == "open_orders":
        print(bot.get_open_orders(symbol=args.symbol))
        return

    if args.action == "cancel":
        if not args.order_id:
            p.error("--order_id is required for cancel")
        print(bot.cancel_order(symbol=args.symbol, order_id=args.order_id))
        return

    if args.action == "trades":
        print(bot.get_trade_history(symbol=args.symbol, limit=args.limit))
        return

    # action=trade
    if not (args.side and args.type and args.qty):
        p.error("--side, --type, and --qty are required for trade")

    if args.type == "MARKET":
        resp = bot.place_market_order(args.symbol, args.side, args.qty)
    elif args.type == "LIMIT":
        if not args.price:
            p.error("--price is required for LIMIT")
        resp = bot.place_limit_order(args.symbol, args.side, args.qty, args.price)
    else:  # STOP
        if not (args.price and args.stop_price):
            p.error("--price and --stop_price required for STOP")
        resp = bot.place_stop_limit(
            args.symbol, args.side, args.qty,
            stop_price=args.stop_price, limit_price=args.price
        )

    print("Order response:", resp)

if __name__ == "__main__":
    main()
