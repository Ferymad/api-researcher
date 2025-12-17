from agency_swarm import Agent, ModelSettings
from openai.types.shared import Reasoning


ceo = Agent(
    name="CEO",
    description="Research orchestrator who receives user concepts, creates research strategy, delegates to api_deep_researcher, and synthesizes findings into structured documentation",
    instructions="./instructions.md",
    model="gpt-5.2",
    model_settings=ModelSettings(
        reasoning=Reasoning(effort="high", summary="auto"),
    ),
)
