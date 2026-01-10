import streamlit as st
from backend.sql_queries import get_daily_summary, get_range_summary
from openai import OpenAI
import pandas as pd
from datetime import date

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])  # or use environment variable


st.header("AI Productivity Insights")

analysis_mode = st.radio(
    "Choose an AI analysis mode:",
    ["Analyze My Day", "Analyze a Date Range"]
)

top_n = st.sliderst.sidebar.slider(
    "Activities For AI Analysis",
    min_value=3,
    max_value=30,
    value=5,
)

#Daily AI Analysis
if analysis_mode == "Analyze My Day":
    selected_day = st.date_input("Select a day", value=date.today())
    df = get_daily_summary(selected_day)

    if df.empty:
        st.warning("No activity logged on this day.")
    else:
        df = df.nlargest(top_n, "total_minutes")

        if st.button("Generate AI Analysis for This Day"):
            csv = df.to_csv(index=False)

            prompt = f"""
            You are an AI productivity assistant. Analyze the user's activity data for {selected_day}.

            Here is the activity summary (activity and minutes spent):

            {csv}

            Provide:
            1. A short summary of the user's day
            2. Productivity strengths
            3. Distractions or inefficiencies
            4. Behavioral patterns you notice
            5. Suggestions for improving tomorrow

            Be concise but insightful.
            """

            with st.spinner("Analyzing your day..."):
                response = client.chat.completions.create(
                    model="gpt-4.1",
                    messages=[{"role": "user", "content": prompt}]
                )

            st.subheader("AI Analysis of The Day")
            st.write(response.choices[0].message["content"])
