# weather_server.py
from fastapi import FastAPI
from fastmcp import FastMCP

# 1. Create your standard FastAPI application
app = FastAPI(title="Weather API", description="A simple weather service")

# 2. Define FastAPI routes with docstrings and type hints
@app.get("/weather/current", operation_id="get_current_weather")
def get_current_weather(city: str) -> dict:
    """Get the current weather for a specified city."""
    # Simulated weather database
    mock_weather = {
        "london": {"temperature": 15, "condition": "Cloudy", "humidity": 75},
        "tokyo": {"temperature": 22, "condition": "Sunny", "humidity": 50},
        "new york": {"temperature": 18, "condition": "Breezy", "humidity": 60},
        "paris": {"temperature": 19, "condition": "Partly Cloudy", "humidity": 65},
    }
    data = mock_weather.get(city.lower(), {"temperature": 20, "condition": "Clear", "humidity": 55})
    return {
        "city": city.title(),
        "temperature_celsius": data["temperature"],
        "condition": data["condition"],
        "humidity_percent": data["humidity"],
    }

@app.get("/weather/forecast", operation_id="get_weather_forecast")
def get_weather_forecast(city: str, days: int = 3) -> dict:
    """Get weather forecast for a specified number of days (1 to 5 days)."""
    forecast = []
    base_temp = 20
    for day in range(1, min(days, 5) + 1):
        forecast.append({
            "day": f"Day {day}",
            "temperature_celsius": base_temp + day,
            "condition": "Sunny" if day % 2 == 0 else "Partly Cloudy"
        })
    return {
        "city": city.title(),
        "forecast_days": days,
        "forecast": forecast
    }

# 3. THE MAGIC LINE: Convert the entire FastAPI app into an MCP Server!
mcp = FastMCP.from_fastapi(app, name="Weather Service")

if __name__ == "__main__":
    # Runs as a network/remote server on port 8000 with Streamable HTTP transport
    mcp.run(transport="http", host="127.0.0.1", port=8000)