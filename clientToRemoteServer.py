# clientToRemoteServer.py
import asyncio
from fastmcp import Client

# 1. Your live FastMCP Cloud URL & API Key
CLOUD_URL = "https://weather-mcp-server-deploy.fastmcp.app/mcp"
API_KEY = "fmcp_0JR-HAt7vjuXc_nV0FKdyUMciRjW6SyqVNirgW31o3w"

async def main():
    print(f"🌐 Connecting to FastMCP Cloud: {CLOUD_URL}...\n")

    # 2. Connect over public HTTPS with authentication
    async with Client(CLOUD_URL, auth=API_KEY) as client:
        
        # 3. Discover remote tools
        print("🔍 Discovering tools available on the Cloud Server:")
        tools = await client.list_tools()
        for tool in tools:
            print(f"  • Tool: {tool.name}")
            print(f"    Description: {tool.description}")
            print("-" * 40)

        # 4. Call 'get_current_weather' remotely
        print("\n⚡ Executing remote call: get_current_weather(city='Tokyo')...")
        weather_result = await client.call_tool("get_current_weather", {"city": "Tokyo"})
        print(f"🌤️ Tokyo Current Weather: {weather_result.content[0].text}")

        # 5. Call 'get_weather_forecast' remotely
        print("\n⚡ Executing remote call: get_weather_forecast(city='London', days=3)...")
        forecast_result = await client.call_tool("get_weather_forecast", {"city": "London", "days": 3})
        print(f"📅 London 3-Day Forecast: {forecast_result.content[0].text}")

if __name__ == "__main__":
    asyncio.run(main())