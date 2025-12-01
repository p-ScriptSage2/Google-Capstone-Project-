# services/route_optimizer.py
from typing import List, Dict

def build_daily_plan(trails: List[Dict], days: int) -> List[Dict]:
    """
    Greedy partitioning of trail durations into 'days' buckets.
    This is simple but deterministic for demo purposes.
    Replace with TSP or constrained optimization for production.
    """
    # convert to hours
    durations = [t.get("duration_hours", 4) for t in trails]
    total_hours = sum(durations)
    target = max(4, int(round(total_hours / days)))  # aim per-day hours

    plans = []
    current = {"legs": [], "total_hours": 0}
    current_hours = 0
    for t in trails:
        dur = t.get("duration_hours", 4)
        if current_hours + dur > target and len(plans) < days - 1:
            plans.append(current)
            current = {"legs": [], "total_hours": 0}
            current_hours = 0
        current["legs"].append({"trail_id": t["id"], "name": t["name"], "duration": dur})
        current["total_hours"] += dur
        current_hours += dur
    plans.append(current)
    # pad days if needed
    while len(plans) < days:
        plans.append({"legs": [], "total_hours": 0})
    return plans
