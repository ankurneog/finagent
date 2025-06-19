from pipelines import  WorkflowState
from agents.base_agent import Agent
import pandas as pd
from typing import Dict
from data.fin_data_defs import FinancialRatios

import ollama  
# Liquidity Agent with LLM integration
class LiquidityAgent(Agent):
    def __init__(self, data_interface, model_name: str = "llama3:8b"):
        super().__init__(
            name="LiquidityAgent",
            description="Analyzes liquidity ratios using LLaMA-3.",
            data_interface=data_interface
        )
        self.next_agents = ["SupervisorAgent"]
        self.model_name = model_name
        self.thresholds = {
            FinancialRatios.CURRENT_RATIO.value: {'healthy': (1.5, 3.0), 'weak': 1.0},
            FinancialRatios.QUICK_RATIO.value: {'healthy': 1.0, 'weak': 1.0},
            FinancialRatios.DEBT_TO_EQUITY.value: {'healthy': (0.3, 1.5), 'weak': 2.0}
        }

    async def execute(self, state: WorkflowState) -> str:
        if state.ratios.empty:
            raise ValueError("No ratios available.")
        
        liquidity_ratios = {
            key: value for key, value in state.ratios.iloc[0].items()
            if key in self.thresholds
        }
        state.update(liquidity_ratios=liquidity_ratios)
        
        # Generate comments using LLaMA-3
        prompt = self._build_prompt(liquidity_ratios, self.thresholds)
        comments = await self._call_llm(prompt)
        state.update(liquidity_comments=comments)
        return f"Liquidity analysis for {state.ticker} complete. Comments: {comments}. Handing off to {self.next_agents}."

    def _build_prompt(self, ratios: Dict, thresholds: Dict) -> str:
        prompt = f"You are a financial analyst evaluating liquidity ratios for a company. Below are the ratios and their thresholds:\n\n"
        for ratio, value in ratios.items():
            thresh = thresholds[ratio]
            if isinstance(thresh['healthy'], tuple):
                prompt += f"{ratio}: {value if value is not None else 'N/A'} (Healthy: {thresh['healthy'][0]}-{thresh['healthy'][1]}, Weak: <{thresh['weak']})\n"
            else:
                prompt += f"{ratio}: {value if value is not None else 'N/A'} (Healthy: >{thresh['healthy']}, Weak: <{thresh['weak']})\n"
        prompt += "\nProvide a detailed analysis of these ratios, including their implications for the company's liquidity. Assign a score (0-10) for each ratio and summarize the overall liquidity. Use clear, professional language."
        return prompt

    async def _call_llm(self, prompt: str) -> str:
        try:
            response = ollama.chat(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}]
            )
            return response['message']['content']
        except Exception as e:
            return f"Error calling LLM: {e}"
