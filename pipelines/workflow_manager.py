from typing import Dict
#from agents import Agent
from pipelines import WorkflowState
from tools.archive import ArchiveManager

class AgentWorkflow:
    def __init__(self, agents, root_agent: str, archiver = ArchiveManager):
        """
        This is the AgentWorkflow class that manages the execution of a sequence of agents.
        It initializes with a dictionary of agents and a root agent to start the workflow.
        :param agents: Dictionary of agent instances keyed by their names.
        """
        self.agents = agents
        self.root_agent = root_agent
        self.state = WorkflowState()
        self.archiver = archiver

    async def run(self, ticker: str) -> str:
        """
        Runs the workflow starting from the root agent, passing the ticker symbol through the agents.
        :param ticker: The stock ticker symbol to analyze.
        :return: Overall commentary from the workflow.
        
        This method initializes the workflow state with the ticker symbol, executes the root agent,"""
        self.state.ticker = ticker
        current_agent = self.agents[self.root_agent]
        
        while current_agent:
            print(f"Executing {current_agent.name}...")
            result = await current_agent.execute(self.state)
            print(result)
            self.archiver.save_commentary(result)

            
            if not current_agent.next_agents:
                break
            
            next_agent_name = current_agent.next_agents[0]  # Simple handoff
            current_agent = self.agents.get(next_agent_name)
        
        return self.state.overall_comments
