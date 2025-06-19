import yfinance as yf  
from data import BaseProvider
from data.fin_data_defs import FinancialRatios
import pandas as pd
from enum import Enum

class YFinanceProvider(BaseProvider):
    """
    YFinanceProvider is a concrete implementation of BaseProvider that uses the yfinance library
    to fetch stock data.
    """
    def __init__(self):
        super().__init__()
        print(f'Source : https://finance.yahoo.com/quote/')
    
    def get_price_history(self, ticker, period="1y", interval="1d"):
        stock = yf.Ticker(ticker)
        return stock.history(period=period, interval=interval)

    def get_company_data(self, ticker):
        '''Fetches company data for a given ticker symbol using yfinance.'''
        stock = yf.Ticker(ticker)
        company_name = stock.info.get('longName', 'Company name not found')
        print(f"Company  : {company_name} ({ticker})")
        info_df = pd.DataFrame.from_dict(stock.info, orient='index', columns=['Value'])
        return info_df
    
    def get_financial_ratios(self, ticker):

        stock = yf.Ticker(ticker)
        ratios = stock.info
        if not ratios:
            print(f"No financial ratios found for {ticker}.")
            return {}

        financial_ratios = {
            FinancialRatios.ROA.value: ratios.get('returnOnAssets', None),
            FinancialRatios.ROE.value: ratios.get('returnOnEquity', None),
            FinancialRatios.NET_PROFIT_MARGIN.value: ratios.get('profitMargins', None),
            FinancialRatios.GROSS_MARGIN.value: ratios.get('grossMargins', None),
            FinancialRatios.CURRENT_RATIO.value: ratios.get('currentRatio', None),
            FinancialRatios.QUICK_RATIO.value: ratios.get('quickRatio', None),
            FinancialRatios.DEBT_TO_EQUITY.value: ratios.get('debtToEquity', None),
            FinancialRatios.INTEREST_COVERAGE.value: None  # Requires income statement
        }
        print(f"Extracted ratios for {ticker}: {financial_ratios}")
        return financial_ratios
    
