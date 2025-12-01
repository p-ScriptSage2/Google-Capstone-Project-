# agents/trail_discovery_agent.py
from typing import List, Dict
from tools.trail_api_tool import TrailAPITool

class TrailDiscoveryAgent:
    @staticmethod
    def find_trails(prefs: Dict) -> List[Dict]:
        """
        Query TrailAPITool (mocked) to return candidate trails.
        Ranking is performed simply for demo purposes.
        """
        region = prefs.get("region")
        difficulty = prefs.get("fitness_level")
        trails = TrailAPITool.search_trails(region=region, difficulty=difficulty)
        ranked = sorted(trails, key=lambda t: (-t.get("scenic_score", 0), t.get("duration_hours", 99)))
        return ranked
