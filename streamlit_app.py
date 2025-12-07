import streamlit as st
import pandas as pd


chart = st.Page("pages/chart.py", title = "Chart", icon = "📊")
#chatbot = st.Page("pages/chatbot.py", title = "Chatbot", icon = "🤖")

pg = st.navigation([chart])

pg.run()