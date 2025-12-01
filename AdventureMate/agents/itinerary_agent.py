# agents/itinerary_agent.py
from typing import Dict, List
from services.route_optimizer import build_daily_plan
from tools.checklist_tool import ChecklistTool

class ItineraryAgent:
    @staticmethod
    def create_itinerary(prefs: Dict, trails: List[Dict], weather: Dict) -> Dict:
        """
        Create a day-by-day itinerary using route optimizer.
        Attach a packing checklist and weather advisory per leg.
        """
        days = prefs.get("duration_days", 3)
        # Select top N trails for planning
        candidates = trails[: max(days * 2, len(trails))]
        daily = build_daily_plan(candidates, days)
        # Attach weather and trail meta to each leg
        for day in daily:
            for leg in day.get("legs", []):
                tid = leg.get("trail_id")
                leg["weather"] = weather.get(tid, {"summary": "unknown"})
        checklist = ChecklistTool.generate_checklist(prefs, days)
        itinerary = {
            "user_prefs": prefs,
            "days": daily,
            "checklist": checklist,
            "meta": {"generator": "ItineraryAgent", "version": "1.0"}
        }
        return itinerary
