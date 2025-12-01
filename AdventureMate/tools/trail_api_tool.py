# tools/trail_api_tool.py
from typing import List, Dict

class TrailAPITool:
    @staticmethod
    def search_trails(region: str = None, difficulty: str = None) -> List[Dict]:
        """
        Mocked trail dataset for the demo. Replace with real API calls later.
        The function returns a list of trail dicts with id, name, location, duration_hours, scenic_score.
        """
        mock = [
            {"id": "t1", "name": "Pine Ridge Loop", "location": "Manali", "duration_hours": 6, "difficulty": "moderate", "scenic_score": 8},
            {"id": "t2", "name": "Valley View Trek", "location": "Manali", "duration_hours": 10, "difficulty": "moderate", "scenic_score": 9},
            {"id": "t3", "name": "River Bend Trail", "location": "Uttarakhand", "duration_hours": 4, "difficulty": "easy", "scenic_score": 7},
            {"id": "t4", "name": "Sunrise Ridge", "location": "Uttarakhand", "duration_hours": 8, "difficulty": "moderate", "scenic_score": 10},
            {"id": "t5", "name": "Alpine Pass", "location": "Manali", "duration_hours": 12, "difficulty": "hard", "scenic_score": 9}
        ]
        if region:
            region_key = region.split(",")[0].strip().lower()
            mock = [m for m in mock if region_key in m["location"].lower()]
        if difficulty:
            # loose matching
            mock = [m for m in mock if m["difficulty"] == difficulty or difficulty == "moderate"]
        return mock
