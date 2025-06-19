import pandas as pd
import argparse
import yfinance as yf  # Ensure yfinance is imported


class Ticker:
    def __init__(self, ticker_symbol):
        self.ticker_symbol = ticker_symbol
        self.data = self.fetch_data()

    def fetch_data(self):
        ticker_data = yf.Ticker(self.ticker_symbol)
        info = ticker_data.info
        df = pd.DataFrame.from_dict(info, orient='index', columns=['Value'])
        return df

def parse_arguments():
    parser = argparse.ArgumentParser(description='Fetch stock data for a given ticker symbol.')
    parser.add_argument('--symbol', type=str, required=True, help='The ticker symbol of the stock')  # Changed to optional argument with `--`
    return parser.parse_args()

def main():
    args = parse_arguments()       
    ticker = Ticker(args.symbol)
    print(ticker.data)

if __name__ == "__main__":
    main()