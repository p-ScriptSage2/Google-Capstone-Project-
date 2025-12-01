# tools/checklist_tool.py
from typing import List

class ChecklistTool:
    @staticmethod
    def generate_checklist(prefs: dict, trip_days: int) -> List[str]:
        checklist = [
            "Water bottle (2L+)",
            "Hiking shoes",
            "Sun protection (sunscreen, hat)",
            "Basic first-aid kit",
            "Personal ID and permits (if required)"
        ]
        if trip_days > 1:
            checklist.append("Sleeping bag and lightweight shelter")
        if prefs.get("fitness_level") == "hard":
            checklist.append("Trekking poles")
        if prefs.get("budget") == "low":
            checklist.append("Budget-friendly snacks")
        return checklist
