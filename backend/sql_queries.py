import sqlite3
import pandas as pd


database = "activity.db"

def get_daily_summary(day):
    #Return a DataFrame: activity vs total elapsed time for a specific day. 
    try:
        with sqlite3.connect(database) as conn:
            query = """
            SELECT 
                activity,
                SUM(elapsed_time_in_minutes) AS total_minutes
            FROM activity_sessions
            WHERE date = ?
            GROUP BY activity
            ORDER BY total_minutes DESC;
            """
    
            df = pd.read_sql_query(query, conn, params=(day,))
            return df
    
    except sqlite3.OperationalError as e:
        print(f'Error: {e}')

def get_range_summary(start_date, end_date):
    """Return activity totals for an inclusive date range."""   
    try:
        with sqlite3.connect(database) as conn:
            query = """
            SELECT 
                activity,
                SUM(elapsed_time_in_minutes) AS total_minutes
            FROM activity_sessions
            WHERE date BETWEEN ? AND ?
            GROUP BY activity
            ORDER BY total_minutes DESC;
            """
    
            df = pd.read_sql_query(query, conn, params=(start_date, end_date))
            return df
    
    except sqlite3.OperationalError as e:
        print(f'Error: {e}')
