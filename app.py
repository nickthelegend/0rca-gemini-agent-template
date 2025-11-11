import os
from orca_agent_sdk import AgentConfig, AgentServer
from agno.agent import Agent
from agno.models.google import Gemini

# Initialize Gemini agent
agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    markdown=True,
    instructions="You are a pirate agent. Respond to all requests in pirate speak with 'Ahoy!' and use pirate terminology like 'matey', 'ye', 'aye', and 'arrr'. Be helpful but maintain your pirate persona at all times."
)

def handle_task(job_input: str) -> str:
    """Use Gemini agent to process the job input"""
    try:
        response = agent.run(job_input)
        return response.content if hasattr(response, 'content') else str(response)
    except Exception as e:
        return f"Error processing request: {str(e)}"

if __name__ == "__main__":
    config = AgentConfig(
        agent_id="5bbf48cf-62a2-4ab3-bd96-1d29ba0fc1f3",
        receiver_address="A3CF2JITRAFHO3SLZ5CSY4AGRU6LBQNZODNRZDKTW5ON5VROFAYYJZA3VA",
        price_microalgos=1_000_000,
        agent_token="28419644f65d92acffbc663a46de10ae41caf8bafd58e686c6f5461ab4256b37",
        remote_server_url="http://localhost:3000/api/agent/access"
    )

    AgentServer(config=config, handler=handle_task).run()