"""
This is the main base class for the agent system.
Keep boiler plate code here 
(c) 2025 Ankur Neog
"""
from pipelines import WorkflowState
class Agent:
    def __init__(self, name: str, description: str, data_interface, next_agents: list = None):
        self.name = name
        self.description = description
        self.data_interface = data_interface
        self.next_agents = next_agents or []

    async def execute(self, state: WorkflowState) -> str:
        raise NotImplementedError("Subclasses must implement execute()")
