# main.py
"""
Orchestrator entrypoint for AdventureMate demo.
Runs a sample planning session using mocked tools and agents.
"""
from agents.preference_interpreter import PreferenceInterpreter
from agents.trail_discovery_agent import TrailDiscoveryAgent
from agents.weather_agent import WeatherAgent
from agents.itinerary_agent import ItineraryAgent
from agents.memory_agent import MemoryAgent
from agents.replanning_agent import ReplanningAgent

def run_sample_session(user_input: str, user_id: str = "demo_user"):
    print("[Orchestrator] Starting session")
    prefs = PreferenceInterpreter.parse(user_input)
    print(f"[Orchestrator] Preferences: {prefs}")

    mem = MemoryAgent(user_id)
    mem.load()

    trails = TrailDiscoveryAgent.find_trails(prefs)
    print(f"[Orchestrator] Found {len(trails)} trails (top 5 shown): {trails[:5]}")

    forecasts = WeatherAgent.fetch_forecasts(trails)
    print(f"[Orchestrator] Fetched {len(forecasts)} forecasts")

    itinerary = ItineraryAgent.create_itinerary(prefs, trails, forecasts)
    print("[Orchestrator] Itinerary created")

    mem.save_trip(itinerary)
    print("[Orchestrator] Itinerary saved to memory")

    replanner = ReplanningAgent()
    updated = replanner.check_and_replan(itinerary)
    if updated:
        print("[Orchestrator] Itinerary updated by replanning agent")

    print("[Orchestrator] Session complete")
    return itinerary

if __name__ == "__main__":
    sample_input = "4-day moderate trek near Manali for 2 people, mid-May, budget friendly"
    plan = run_sample_session(sample_input)
    import json
    print(json.dumps(plan, indent=2))
