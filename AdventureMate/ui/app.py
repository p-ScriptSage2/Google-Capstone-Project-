# ui/app.py

import sys
import os
import streamlit as st

# Fix: ensure project root is importable
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from main import run_sample_session

# Streamlit page config
st.set_page_config(page_title="AdventureMate Demo", layout="centered")

# App header
st.title("AdventureMate — Adventure Travel Planner")

# OPTIONAL SAMPLE BUTTON (fixed: removed missing argument call)
if st.button("Run Sample Session"):
    st.info("Running sample session...")
    itinerary = run_sample_session({"demo": True})
    st.success("Sample itinerary generated")
    st.write(itinerary)

# Trip planning form
with st.form("trip_form"):
    user_text = st.text_area(
        "Describe your trip (region, duration, preferences):",
        value="4-day moderate trek near Manali for 2 people, mid-May, budget friendly"
    )
    user_id = st.text_input("User ID (for memory)", value="demo_user")
    submitted = st.form_submit_button("Plan my trip")

if submitted:
    st.info("Planning in progress...")

    # FIX: Always pass user_input dict so run_sample_session never errors
    user_input = {"text": user_text, "user_id": user_id}

    itinerary = run_sample_session(user_input)

    st.success("Itinerary generated")

    st.subheader("Packing checklist")
    st.write(itinerary.get("checklist", []))

    st.subheader("Day-by-day plan")
    for i, d in enumerate(itinerary.get("days", []), start=1):
        st.markdown(f"**Day {i} — total hours: {d.get('total_hours', 0)}**")

        for leg in d.get("legs", []):
            st.markdown(
                f"- {leg.get('name')} ({leg.get('duration')} hrs) — "
                f"Weather: {leg.get('weather', {}).get('summary', 'N/A')}"
            )

        if d.get("notes"):
            st.markdown("**Notes:**")
            for n in d["notes"]:
                st.write(f"- {n}")
    st.write("---")
