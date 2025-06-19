def get_ticker(args):
    if args.country == "US":
        return args.symbol.upper()
    elif args.country == "IN":
        return args.symbol.upper() + ".NS"
    else:
        raise ValueError("Unsupported country. Use 'US' or 'IN'.")