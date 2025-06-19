from pipelines import  WorkflowState
from agents.base_agent import Agent
import pandas as pd

class FundamentalAgent(Agent):
    def __init__(self,data_interface):
        super().__init__(
            name="FundamentalAgent",
            description="Fetches fundamental financial ratios for a given ticker.",
            data_interface=data_interface
        )
        self.next_agents = ["ProfitabilityAgent", "LiquidityAgent"]

    async def execute(self, state: WorkflowState) -> str:
        if not state.ticker:
            raise ValueError("Ticker not set in state.")
        
        financial_ratios = self.data_interface.get_financial_ratios(state.ticker)
        if financial_ratios is None or not financial_ratios:
            raise ValueError(f"No financial ratios found for ticker {state.ticker}.")
        
        state.update(ratios=pd.DataFrame([financial_ratios]))
        return f"Ratios extracted for {state.ticker}. Handing off to {self.next_agents}."

