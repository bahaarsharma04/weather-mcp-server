# cloud_proxy.py
import os
from fastmcp import Client
from fastmcp.server import create_proxy

# Your live FastMCP Cloud URL
CLOUD_URL = "https://weather-mcp-server-deploy.fastmcp.app/mcp"

# Your Horizon API Key
API_KEY = os.environ.get("HORIZON_API_KEY", "fmcp_0JR-HAt7vjuXc_nV0FKdyUMciRjW6SyqVNirgW31o3w")

# Create authenticated client connected to your cloud deployment
client = Client(CLOUD_URL, auth=API_KEY)

# Create a local proxy so Claude Desktop can talk to it seamlessly via stdio
proxy = create_proxy(client)

if __name__ == "__main__":
    proxy.run()
