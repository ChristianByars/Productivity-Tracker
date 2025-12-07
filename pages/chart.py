import streamlit as st
from datetime import date
import pandas as pd

from backend.sql_queries import get_daily_summary, get_range_summary

#title
st.title("📊 Productivity Activity Dashboard")


#Side bar
st.sidebar.header("Views")

view_mode = st.sidebar.radio(
    "Select Mode",
    ["Daily Summary", "Date Range Summary"]
)

# Top-N slider
top_n = st.sidebar.slider(
    "Show Top Activities",
    min_value=3,
    max_value=30,
    value=5,
)

#daily summary
if view_mode == "Daily Summary":
    selected_day = st.date_input(
        "Select a day",
        value=date.today()
    )

    st.subheader(f"Daily Summary — {selected_day}")

    df = get_daily_summary(selected_day)

    if df.empty:
        st.info("No activity logged on this day.")
    else:
        df_top_N_activities = df.nlargest(top_n, "total_minutes")
        st.bar_chart(
            df_top_N_activities,
            x = "activity",
            y = "total_minutes",
            x_label= "Activity",
            y_label= "Time in Minutes"
        )



#date range summary
elif view_mode == "Date Range Summary":
    start_date = st.date_input("Start Date", value=date.today())
    end_date = st.date_input("End Date", value=date.today())

    if start_date > end_date:
        st.error("Start date must be before end date.")
    else:
        st.subheader(f"Summary for {start_date} to {end_date}")

        df = get_range_summary(start_date, end_date)

        if df.empty:
            st.info("No activity found in this range.")
        else:
            df_top = df.nlargest(top_n, "total_minutes")
            st.bar_chart(
            df_top,
            x = "activity",
            y = "total_minutes",
            x_label= "Activity",
            y_label= "Time in Minutes"
        )


#Raw data table
if not df.empty and st.checkbox("Show Raw Data Table"):
    st.dataframe(df)
