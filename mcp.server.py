from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os
from exa_py import Exa

load_dotenv()
mcp = FastMCP("websearch")
exa = Exa(api_key=os.getenv("EXA_API_KEY"))

@mcp.tool()
async def search_web(query: str, num_results: int = 5) -> str:
    results = exa.search_and_contents(query, summary={"query": "Main points"}, num_results=num_results)
    output = ""
    for r in results:
        output += f"\n- [{r.title}]({r.url})\n  - {r.publication_date}\n  - {r.content[:200]}..."
    return output

if __name__ == "__main__":
    mcp.run()