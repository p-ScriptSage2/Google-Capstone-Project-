# tools/map_tool.py
def estimate_travel_time_km(distance_km: float, mode: str = "drive") -> float:
    """
    Simple heuristic: driving 40 km/h average, walking 5 km/h.
    Returns hours.
    """
    if mode == "walk":
        return distance_km / 5.0
    return distance_km / 40.0
