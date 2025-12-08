# Productivity Activity Tracker

A activity tracking software that monitors your active window or browser tab and visualizes your activity data using a Streamlit dashboard.

This project consists of two main components:

1. **The Tracker** — continuously logs your foreground activity.
2. **The Dashboard** — visualizes logged data through Streamlit.

---

## Features

- Tracks active applications and/or window text changes  
- Records session duration 
- Logs sessions into SQLite for long-term analysis  
- Streamlit dashboard provides:
  - Daily summaries  
  - Date-range summaries  
  - Top-N activity visualization
  - Raw Data  
- Filtering to eliminate flicker, system noise, blank titles.

## To run tracker

```bash
python __main__.py
```

## To get visualizations
```bash
streamlit run streamlit_app.py
```
Just make sure you are in the right directory when running the scripts. Enjoy!
