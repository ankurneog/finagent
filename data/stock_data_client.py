from data import YFinanceProvider, FMPProvider, BaseProvider
from os import getenv

class StockDataClient:
    def __init__(self, provider : str):
        if provider == "yfinance":
            self.provider = YFinanceProvider()
        elif provider == "fmp":
            self.provider = FMPProvider(api_key=getenv("FMP_API_KEY"))
        else:
            raise ValueError("Unsupported provider. Use 'yfinance' or 'fmp'.")

    def get_price_history(self, ticker, period="1y", interval="1d"):
        return self.provider.get_price_history(ticker, period, interval)

    def get_company_data(self, ticker):
        return self.provider.get_company_data(ticker)
    
    def get_financial_ratios(self, ticker):
        return self.provider.get_financial_ratios(ticker)
