from dotenv import load_dotenv
from agency_swarm import Agency
from ceo import ceo
from api_deep_researcher import api_deep_researcher

load_dotenv()


def create_agency(load_threads_callback=None):
    """Create and return the deep_researcher agency instance.

    This function is required for deployment.
    """
    agency = Agency(
        ceo,  # Entry point - receives user messages
        communication_flows=[
            (ceo, api_deep_researcher),  # CEO delegates research tasks to api_deep_researcher
        ],
        shared_instructions="shared_instructions.md",
    )
    return agency


if __name__ == "__main__":
    agency = create_agency()
    agency.terminal_demo()

    # For programmatic testing:
    # response = agency.get_response_sync("your test query")
    # print(response)
