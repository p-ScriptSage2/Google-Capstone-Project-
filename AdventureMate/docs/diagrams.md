# Architecture (Mermaid)

```mermaid
flowchart LR
  UI[User UI (Streamlit)] --> Orch[Orchestrator (main.py)]
  Orch --> Pref[Preference Interpreter]
  Orch --> TD[Trail Discovery Agent]
  Orch --> WA[Weather Agent]
  TD --> Tools[Trail API / Map Tools]
  WA --> Tools
  Orch --> Itin[Itinerary Synthesizer]
  Itin --> Route[Route Optimizer (services)]
  Orch --> Memory[Memory Agent]
  Orch --> Replan[Replanning Agent (Loop)]
  Orch --> Booking[Booking Assistant (mock)]
  Booking --> MockBooking[Mock Booking API]
