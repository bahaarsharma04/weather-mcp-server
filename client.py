# client.py
import asyncio
from pathlib import Path
from fastmcp import Client

async def main():
    print("🔌 Connecting to MCP Server as a Client...\n")

    # 1. Connect to our local server via standard I/O
    async with Client(Path("local_server.py")) as client:
        
        # 2. Discover available tools (Handshake & Discovery)
        print("🔍 Discovering available tools from server:")
        tools = await client.list_tools()
        for tool in tools:
            print(f"  • Tool Name: {tool.name}")
            print(f"    Description: {tool.description}")
            print(f"    Parameters: {tool.input_schema}")
            print("-" * 40)

        # 3. Call a tool programmatically with arguments
        print("\n⚡ Calling 'multiply_numbers' with arguments a=15, b=4...")
        result = await client.call_tool("multiply_numbers", {"a": 15, "b": 4})
        
        # 4. Print the raw output returned by the server
        print(f"✅ Result from Server: {result.content[0].text}")

if __name__ == "__main__":
    asyncio.run(main())