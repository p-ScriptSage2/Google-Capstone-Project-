# ui/app.py

import streamlit as st
import threading
# ui/app.py
import sys
import os

# Add parent folder to Python path so main.py can be imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now import main.py
from main import run_sample_session

import streamlit as st

# Example usage
st.title("AdventureMate App")
if st.button("Run Sample Session"):
    run_sample_session()


st.set_page_config(page_title="AdventureMate Demo", layout="centered")
st.title("AdventureMate — Adventure Travel Planner ")

with st.form("trip_form"):
    user_text = st.text_area("Describe your trip (region, duration, preferences):",
                             value="4-day moderate trek near Manali for 2 people, mid-May, budget friendly")
    user_id = st.text_input("User ID (for memory)", value="demo_user")
    submitted = st.form_submit_button("Plan my trip")

if submitted:
    st.info("Planning in progress (demo uses mocked data).")
    def run_and_display():
        itinerary = run_sample_session(user_text, user_id)
        st.success("Itinerary generated (see below)")
        st.subheader("Packing checklist")
        st.write(itinerary.get("checklist", []))
        st.subheader("Day-by-day plan")
        for i, d in enumerate(itinerary.get("days", []), start=1):
            st.markdown(f"**Day {i} — total hours: {d.get('total_hours', 0)}**")
            for leg in d.get("legs", []):
                st.markdown(f"- {leg.get('name')} ({leg.get('duration')} hrs) — Weather: {leg.get('weather', {}).get('summary')}")
            if d.get("notes"):
                st.markdown("**Notes:**")
                for n in d["notes"]:
                    st.write(f"- {n}")
        st.write("---")
    t = threading.Thread(target=run_and_display)
    t.start()
