import sqlite3


database = "activity.db"

#initial table for primary functionality
tables = [
    """CREATE TABLE IF NOT EXISTS activity_sessions (
            session_id INTEGER PRIMARY KEY,
            start_time TIME NOT NULL,
            end_time TIME NOT NULL,
            app TEXT NOT NULL,
            window_title TEXT NOT NULL,
            );"""
]

try:
    with sqlite3.connect(database) as conn:
        cursor = conn.cursor()
        
        for table in tables:
            cursor.execute(table)
        conn.commit()
        print("Tables created")
        
except sqlite3.OperationalError as e:
    print("Failed to create database:", e)