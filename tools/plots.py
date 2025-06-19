import matplotlib.pyplot as plt
import yfinance as yf
from tools.archive import ArchiveManager

class TickerPlotter:
    
    def __init__(self, args,am: ArchiveManager):
        self.ticker = args.symbol.upper() + (".NS" if args.country == "IN" else "")
        self.am = am

    def plot_all(self, period: str = '1y'):
        """
        Plots all available stock data for the given ticker symbol over a specified period.
        
        :param period: Period for which to fetch data (e.g., '1y', '6mo', '3mo').
        """
        stock = yf.Ticker(self.ticker)
        data = stock.history(period=period)
        
        fig, axs = plt.subplots(3, 1, figsize=(14, 15))
        
        # Plot Closing Prices
        axs[0].plot(data.index, data['Close'], label='Close Price', color='blue')
        axs[0].set_title(f'{self.ticker} Closing Prices ({period})')
        axs[0].set_xlabel('Date')
        axs[0].set_ylabel('Price (USD)')
        axs[0].legend()
        axs[0].grid()

        # Plot Volume
        axs[1].bar(data.index, data['Volume'], color='orange')
        axs[1].set_title(f'{self.ticker} Trading Volume ({period})')
        axs[1].set_xlabel('Date')
        axs[1].set_ylabel('Volume')
        axs[1].grid()

        # Plot Moving Average
        data['Moving Average'] = data['Close'].rolling(window=20).mean()
        axs[2].plot(data.index, data['Close'], label='Close Price', color='blue')
        axs[2].plot(data.index, data['Moving Average'], label='20-Day Moving Average', color='red')
        axs[2].set_title(f'{self.ticker} Moving Average ({period})')
        axs[2].set_xlabel('Date')
        axs[2].set_ylabel('Price (USD)')
        axs[2].legend()
        axs[2].grid()

        plt.tight_layout()
        plt.show()
        self.am.save_plot(plt, f"{self.ticker}_all_plots_{period}.png")
        return plt

    def plot_historical_prices(self, start_date: str, end_date: str):
        """
        Plots historical stock prices for the given ticker symbol.
        
        :param start_date: Start date for historical data in 'YYYY-MM-DD' format.
        :param end_date: End date for historical data in 'YYYY-MM-DD' format.
        """
        stock = yf.Ticker(self.ticker)
        data = stock.history(start=start_date, end=end_date)
        
        plt.figure(figsize=(14, 7))
        plt.plot(data.index, data['Close'], label='Close Price', color='blue')
        plt.title(f'{self.ticker} Historical Prices')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.grid()
        plt.show()
    
    def plot_historical_prices(self, period: str = '1y'):
        """
        Plots historical stock prices for the given ticker symbol over a specified period.
        
        :param period: Period for which to fetch data (e.g., '1y', '6mo', '3mo').
        """
        stock = yf.Ticker(self.ticker)
        data = stock.history(period=period)
        
        plt.figure(figsize=(14, 7))
        plt.plot(data.index, data['Close'], label='Close Price', color='blue')
        plt.title(f'{self.ticker} Historical Prices ({period})')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.grid()
        plt.show()

    def plot_volume(self, period: str = '1y'):
        """
        Plots trading volume for the given ticker symbol over a specified period.
        
        :param period: Period for which to fetch data (e.g., '1y', '6mo', '3mo').
        """
        stock = yf.Ticker(self.ticker)
        data = stock.history(period=period)
        
        plt.figure(figsize=(14, 7))
        plt.bar(data.index, data['Volume'], color='orange')
        plt.title(f'{self.ticker} Trading Volume ({period})')
        plt.xlabel('Date')
        plt.ylabel('Volume')
        plt.grid()
        plt.show()

    def plot_moving_average(self, period: str = '1y', window: int = 20):
        """
        Plots the moving average of the stock prices for the given ticker symbol.
        
        :param period: Period for which to fetch data (e.g., '1y', '6mo', '3mo').
        :param window: Window size for the moving average.
        """
        stock = yf.Ticker(self.ticker)
        data = stock.history(period=period)
        
        data['Moving Average'] = data['Close'].rolling(window=window).mean()
        
        plt.figure(figsize=(14, 7))
        plt.plot(data.index, data['Close'], label='Close Price', color='blue')
        plt.plot(data.index, data['Moving Average'], label=f'{window}-Day Moving Average', color='red')
        plt.title(f'{self.ticker} Moving Average ({period})')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.grid()
        plt.show()

