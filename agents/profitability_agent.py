from pipelines import  WorkflowState
from agents.base_agent import Agent
import pandas as pd
from typing import Dict
from data.fin_data_defs import FinancialRatios
import ollama  
# Profitability Agent with LLM integration
class ProfitabilityAgent(Agent):
    def __init__(self, data_interface, model_name: str = "llama3:8b"):
        super().__init__(
            name="ProfitabilityAgent",
            description="Analyzes profitability ratios using LLaMA-3.",
            data_interface=data_interface
        )
        self.next_agents = ["LiquidityAgent"]
        self.model_name = model_name
        self.thresholds = {
            FinancialRatios.ROA.value: {'healthy': 0.05, 'moderate': 0.02},
            FinancialRatios.ROE.value: {'healthy': 0.15, 'moderate': 0.08},
            FinancialRatios.NET_PROFIT_MARGIN.value: {'healthy': 0.10, 'moderate': 0.05},
            FinancialRatios.GROSS_MARGIN.value: {'healthy': 0.40, 'moderate': 0.20}
        }

    async def execute(self, state: WorkflowState) -> str:
        if state.ratios.empty:
            raise ValueError("No ratios available.")
        
        profitability_ratios = {
            key: value for key, value in state.ratios.iloc[0].items()
            if key in self.thresholds
        }
        state.update(profitability_ratios=profitability_ratios)
        
        # Generate comments using LLaMA-3
        prompt = self._build_prompt(profitability_ratios, self.thresholds)
        comments = await self._call_llm(prompt)
        state.update(profitability_comments=comments)
        return f"Profitability analysis for {state.ticker} complete. Comments: {comments}. Handing off to {self.next_agents}."

    def _build_prompt(self, ratios: Dict, thresholds: Dict) -> str:
        prompt = f"You are a financial analyst evaluating profitability ratios for a company. Below are the ratios and their thresholds:\n\n"
        for ratio, value in ratios.items():
            thresh = thresholds[ratio]
            prompt += f"{ratio}: {value if value is not None else 'N/A'} (Healthy: >{thresh['healthy']}, Moderate: >{thresh['moderate']})\n"
        prompt += "\nProvide a detailed analysis of these ratios, including their implications for the company's financial health. Assign a score (0-10) for each ratio and summarize the overall profitability. Use clear, professional language."
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
