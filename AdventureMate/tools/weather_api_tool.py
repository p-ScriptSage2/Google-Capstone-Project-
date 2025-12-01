# tools/weather_api_tool.py
import datetime

class WeatherAPITool:
    @staticmethod
    def get_forecast(location: str):
        """
        Return a small, deterministic mock forecast object.
        Replace with real weather API calls using keys in .env when ready.
        """
        return {
            "location": location,
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "summary": "Partly cloudy. Small chance of afternoon rain.",
            "temperature_c": 16
        }
