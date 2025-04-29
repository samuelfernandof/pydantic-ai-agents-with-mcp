import asyncio
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio

async def main():
    agent = Agent.from_mcp_servers([  # Integração dos agentes
        MCPServerStdio("python_tools"),
        MCPServerStdio("websearch")
    ])

    while True:
        user_input = input("Pergunta: ")
        if user_input.lower() in ["sair", "exit"]:
            break
        resposta = await agent.run(user_input)
        print("\nResposta:\n", resposta)

if __name__ == "__main__":
    asyncio.run(main())