from data import BaseProvider
import pandas as pd 
from data import BaseProvider
"""
Dummy code for FMP, we need further enhancement to this, we have to make the 
data uniform with the other providers and also add error handling.
"""

class FMPProvider(BaseProvider):
    def __init__(self, api_key):
        self.api_key = api_key

    def get_price_history(self, ticker, period="1y", interval="1d"):
        url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?apikey={self.api_key}"
        response = requests.get(url)
        data = response.json()
        return data.get("historical", [])

    def get_company_data(self, ticker):
        url = f"https://financialmodelingprep.com/api/v3/profile/{ticker}?apikey={self.api_key}"
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame(data)
        return df
    def get_financial_ratios(self, ticker):
        pass
