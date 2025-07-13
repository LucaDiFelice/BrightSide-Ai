import streamlit as st
import pandas as pd

mood_tab, coach_tab = st.tabs(["Mood", "BrightSide coach"])
finish_button = st.columns([1])

with mood_tab:
    st.header("Log your mood")
    feeling_input = st.text_input("How are you feeling right now?")
    mood_input = st.text_input("How did you feel overall today")
    with finish_button[0]:
        if st.button("Finish", use_container_width=True):
            st.write("Finish button clicked")