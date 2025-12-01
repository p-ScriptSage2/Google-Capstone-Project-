# agents/weather_agent.py
from typing import List, Dict
from tools.weather_api_tool import WeatherAPITool

class WeatherAgent:
    @staticmethod
    def fetch_forecasts(trails: List[Dict]) -> Dict:
        """
        Fetch a forecast per trail location. Returns dict keyed by trail id.
        """
        forecasts = {}
        for t in trails:
            forecasts[t["id"]] = WeatherAPITool.get_forecast(t.get("location", "unknown"))
        return forecasts
