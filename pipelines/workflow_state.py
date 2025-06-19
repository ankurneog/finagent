import pandas as pd

class WorkflowState:
    def __init__(self):
        self.ticker = ""
        self.ratios = pd.DataFrame()
        self.profitability_ratios = {}
        self.liquidity_ratios = {}
        self.profitability_comments = None
        self.liquidity_comments = None
        self.overall_comments = None

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
