# tests/test_route_optimizer.py
from services.route_optimizer import build_daily_plan

def test_build_daily_plan_len_and_hours():
    trails = [
        {"id": "a", "name": "A", "duration_hours": 4},
        {"id": "b", "name": "B", "duration_hours": 4},
        {"id": "c", "name": "C", "duration_hours": 6},
        {"id": "d", "name": "D", "duration_hours": 2}
    ]
    days = 3
    plan = build_daily_plan(trails, days)
    assert len(plan) == days
    total = sum(day["total_hours"] for day in plan)
    assert total == 16
