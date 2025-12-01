# Architecture — AdventureMate

Mermaid diagram is in `docs/diagrams.md`. Key components:

- Master Orchestrator (`main.py`)
- Agents:
  - Preference Interpreter
  - Trail Discovery (parallel)
  - Weather & Safety (parallel)
  - Itinerary Synthesizer (sequential)
  - Replanning Agent (loop)
  - Memory Manager
- Tools:
  - Trail API tool (mocked)
  - Weather API tool (mocked)
  - Map tool (mocked)
  - Checklist generator
- Services:
  - Route optimizer

The system demonstrates multi-agent patterns, tools, sessions & memory, context compaction, observability (print/logs), and a UI for demonstration.
