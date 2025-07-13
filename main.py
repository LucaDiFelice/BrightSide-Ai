import streamlit as st
import pandas as pd
from datetime import date

mood_tab, coach_tab, goals_tab = st.tabs(["Mood", "BrightSide coach", "Goals"])

def main():
    with mood_tab:
        today_date = date.today()
        st.header(today_date)
        feeling_input = st.text_input("How are you feeling right now?")
        mood_input = st.text_input("How did you feel overall today")
        finish_column = st.columns([1])
        with finish_column[0]:
            if st.button("Finish", use_container_width=True):
                st.write("Data sent to ChatGPT")

    with coach_tab:
        st.write("hello")

main()