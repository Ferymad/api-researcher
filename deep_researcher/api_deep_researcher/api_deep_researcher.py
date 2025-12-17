import os
from agency_swarm import Agent, ModelSettings, HostedMCPTool
from openai.types.shared import Reasoning
from agents.mcp import MCPServerStdio, MCPServerSse
from dotenv import load_dotenv

load_dotenv()

# 1. DeepWiki MCP - Remote SSE server for GitHub documentation
deepwiki_server = MCPServerSse(
    name="DeepWiki",
    params={
        "url": "https://mcp.deepwiki.com/sse",
    },
    cache_tools_list=True
)

# 2. Context7 MCP - NPM package for library documentation (33K+ libraries)
context7_server = MCPServerStdio(
    name="Context7",
    params={
        "command": "npx",
        "args": ["-y", "@upstash/context7-mcp"],
        "env": {
            "CONTEXT7_API_KEY": os.getenv("CONTEXT7_API_KEY", "")  # Optional key
        }
    },
    cache_tools_list=True
)

# 3. Exa MCP - NPM package for semantic search and deep research
exa_server = MCPServerStdio(
    name="Exa_Search",
    params={
        "command": "npx",
        "args": ["-y", "exa-mcp-server"],
        "env": {
            "EXA_API_KEY": os.getenv("EXA_API_KEY", "")  # Required - must be set in .env
        }
    },
    cache_tools_list=True
)

# 4. Jina AI MCP - Hosted remote server for URL-to-markdown conversion
jina_api_key = os.getenv("JINA_API_KEY", "")
jina_mcp = HostedMCPTool(
    tool_config={
        "type": "mcp",
        "server_label": "jina-ai",
        "server_url": "https://mcp.jina.ai/",
        "require_approval": "never",
        "headers": {
            "Authorization": f"Bearer {jina_api_key}"
        } if jina_api_key else {}
    }
)

# 5. Brave Search MCP - NPM package for web search
brave_server = MCPServerStdio(
    name="Brave_Search",
    params={
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-brave-search"],
        "env": {
            "BRAVE_API_KEY": os.getenv("BRAVE_API_KEY", "")  # Required - must be set in .env
        }
    },
    cache_tools_list=True
)

api_deep_researcher = Agent(
    name="API Deep Researcher",
    description="Research execution specialist with access to 5 MCP servers for comprehensive API documentation gathering using DeepWiki, Context7, Exa, Jina AI, and Brave Search",
    instructions="./instructions.md",
    files_folder="./files",
    tools_folder="./tools",
    tools=[jina_mcp],  # HostedMCPTool goes in tools parameter
    mcp_servers=[deepwiki_server, context7_server, exa_server, brave_server],  # Other MCP servers
    model="gpt-5.2",
    model_settings=ModelSettings(
        reasoning=Reasoning(effort="medium", summary="auto"),
    ),
)
