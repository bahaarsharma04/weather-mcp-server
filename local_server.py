# local_server.py
from fastmcp import FastMCP
import datetime

# 1. Initialize FastMCP server
mcp = FastMCP("MyFirstLocalServer")

# 2. Define a simple tool
@mcp.tool
def get_system_time() -> str:
    """Returns the current date and time from the local machine."""
    now = datetime.datetime.now()
    return f"The current local system time is: {now.strftime('%Y-%m-%d %H:%M:%S')}"

# 3. Define another tool with parameters
@mcp.tool
def multiply_numbers(a: float, b: float) -> str:
    """Multiplies two numbers together."""
    result = a * b
    return f"The product of {a} and {b} is {result}"

if __name__ == "__main__":
    # Runs the server using standard input/output (stdio)
    mcp.run()