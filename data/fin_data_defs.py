from enum import Enum

class FinancialRatios(Enum):
    """
    Enum representing various financial ratios used for analyzing a company's financial performance.

    Attributes:
        ROA: Return on Assets - Measures how efficiently a company uses its assets to generate profit.
        ROE: Return on Equity - Indicates how well a company uses investments to generate earnings growth.
        NET_PROFIT_MARGIN: Net Profit Margin - Represents the percentage of revenue that remains as profit after all expenses.
        GROSS_MARGIN: Gross Margin - Shows the percentage of revenue that exceeds the cost of goods sold (COGS).
        CURRENT_RATIO: Current Ratio - Measures a company's ability to pay short-term obligations with its current assets.
        QUICK_RATIO: Quick Ratio - Assesses a company's ability to meet its short-term liabilities without relying on inventory sales.
        DEBT_TO_EQUITY: Debt-to-Equity Ratio - Compares a company's total liabilities to its shareholder equity, indicating financial leverage.
        INTEREST_COVERAGE: Interest Coverage Ratio - Evaluates how easily a company can pay interest on its outstanding debt.
    """
    ROA = 'Return on Assets (ROA)'
    ROE = 'Return on Equity (ROE)'
    NET_PROFIT_MARGIN = 'Net Profit Margin'
    GROSS_MARGIN = 'Gross Margin'
    CURRENT_RATIO = 'Current Ratio'
    QUICK_RATIO = 'Quick Ratio'
    DEBT_TO_EQUITY = 'Debt-to-Equity Ratio'
    INTEREST_COVERAGE = 'Interest Coverage Ratio'  # Requires income statement