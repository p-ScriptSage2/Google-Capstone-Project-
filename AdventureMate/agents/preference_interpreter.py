# agents/preference_interpreter.py
from typing import Dict

class PreferenceInterpreter:
    @staticmethod
    def parse(text: str) -> Dict:
        """
        Lightweight heuristic parser.
        In production, replace with an LLM prompt that extracts structured constraints.
        """
        t = text.lower()
        prefs = {
            "duration_days": 3,
            "region": None,
            "adventure_type": "trekking",
            "fitness_level": "moderate",
            "budget": "medium",
            "people": 1,
            "avoid": []
        }
        if "4-day" in t or "4 day" in t or "4-day" in text:
            prefs["duration_days"] = 4
        if "manali" in t:
            prefs["region"] = "Manali, Himachal Pradesh"
        if "uttarakhand" in t:
            prefs["region"] = "Uttarakhand, India"
        if "budget" in t:
            prefs["budget"] = "low"
        if "2 people" in t or "two people" in t or "2 persons" in t:
            prefs["people"] = 2
        if "easy" in t:
            prefs["fitness_level"] = "easy"
        if "hard" in t or "difficult" in t:
            prefs["fitness_level"] = "hard"
        return prefs
