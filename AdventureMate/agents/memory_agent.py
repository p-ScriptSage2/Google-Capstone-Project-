# agents/memory_agent.py
import json
import os
from typing import Dict

class MemoryAgent:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.path = f"memory_{user_id}.json"
        self._data = {"trips": [], "preferences": {}}

    def load(self) -> Dict:
        if os.path.exists(self.path):
            with open(self.path, "r", encoding="utf-8") as f:
                self._data = json.load(f)
        return self._data

    def save_trip(self, itinerary: Dict) -> None:
        self._data.setdefault("trips", []).append(itinerary)
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self._data, f, indent=2, ensure_ascii=False)

    def set_preferences(self, prefs: Dict) -> None:
        self._data["preferences"] = prefs
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self._data, f, indent=2, ensure_ascii=False)
