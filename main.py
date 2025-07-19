import streamlit as st
import pandas as pd
from datetime import date
import time

from ollama import chat
from ollama import ChatResponse

mood_tab, coach_tab, goals_tab = st.tabs(["Mood", "BrightSide coach", "Goals"])

def main():
    feeling_input = None
    mood_input = None
    with mood_tab:
        today_date = date.today()
        st.header(today_date)
        feeling_input = st.text_input("How are you feeling right now?")
        mood_input = st.text_input("How did you feel overall today")
        finish_column = st.columns([1])
        with finish_column[0]:
            if st.button("Finish", use_container_width=True):
                st.write("Data sent to ChatGPT")
                response: ChatResponse = chat(model="deepseek-r1:1.5b", messages=[
                    {
                        "role" : "user",
                        "content" : feeling_input
                    },
                ])
                time.sleep(10)
                st.write(response["message"]["content"])

main()