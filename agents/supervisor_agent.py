from pipelines.workflow_manager import  WorkflowState
from agents.base_agent import Agent
import yfinance as yf
import pandas as pd
from typing import Dict
import ollama 

class SupervisorAgent(Agent):
    def __init__(self, data_interface, model_name: str = "llama3:8b"):
        super().__init__(
            name="SupervisorAgent",
            description="Provides an overall financial health assessment using LLaMA-3.",
            data_interface=data_interface

        )
        self.next_agents = []
        self.model_name = model_name

    async def execute(self, state: WorkflowState) -> str:
        if not state.profitability_comments or not state.liquidity_comments:
            raise ValueError("Incomplete analysis data.")
        
        # Generate overall assessment using LLaMA-3
        prompt = self._build_prompt(state.profitability_comments, state.liquidity_comments)
        overall_comment = await self._call_llm(prompt)
        state.update(overall_comments=overall_comment)
        return f"Overall financial health assessment for {state.ticker}: {overall_comment}"

    def _build_prompt(self, profitability: str, liquidity: str) -> str:
        prompt = f"You are a senior financial analyst synthesizing a company's financial health. Below are the profitability and liquidity analyses:\n\n"
        prompt += f"Profitability Analysis:\n{profitability}\n\nLiquidity Analysis:\n{liquidity}\n\n"
        prompt += "Provide a comprehensive summary of the company's financial health, integrating both analyses. Highlight strengths, weaknesses, and recommendations for investors or management. Use clear, professional language."
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