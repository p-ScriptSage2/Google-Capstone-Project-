# agents/replanning_agent.py
import random
from typing import Dict

class ReplanningAgent:
    """
    Simulated loop agent that checks current itinerary and returns True
    if it applied an update (simulating a weather or closure event).
    In production, this would run periodically or listen to events.
    """
    def check_and_replan(self, itinerary: Dict) -> bool:
        # 10% chance to simulate a change (for demo)
        if random.random() < 0.1:
            # Insert a replanning note on day 1
            if itinerary.get("days"):
                itinerary["days"][0].setdefault("notes", []).append("Replanned due to simulated weather; alternate route suggested.")
            return True
        return False
