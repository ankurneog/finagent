from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """
    Abstract base class for stock data providers.
    
    """
    @abstractmethod
    def get_price_history(self, ticker, period="1y", interval="1d"):
        pass

    @abstractmethod
    def get_company_data(self, ticker):
        pass

    @abstractmethod
    def get_financial_ratios(self, ticker):
        """
        Abstract method to fetch financial ratios for a given ticker.
        This method should be implemented by concrete providers.
        eg:
            financial_ratios = {
            'Return on Assets (ROA)': ratios.get('returnOnAssets', None),
            'Return on Equity (ROE)': ratios.get('returnOnEquity', None),
            'Net Profit Margin': ratios.get('profitMargins', None),
            'Gross Margin': ratios.get('grossMargins', None),
            'Current Ratio': ratios.get('currentRatio', None),
            'Quick Ratio': ratios.get('quickRatio', None),
            'Debt-to-Equity Ratio': ratios.get('debtToEquity', None),
            'Interest Coverage Ratio': None  # Requires income statement
        }
        """
        pass
