import sqlite3


database = "activity.db"

#initial table for primary functionality
tables = [
    """CREATE TABLE IF NOT EXISTS activity_sessions(
            event_id INTEGER PRIMARY KEY AUTOINCREMENT,
            elapsed_time INTEGER NOT NULL,
            app TEXT,
            browser_tab TEXT,
            date TEXT NOT NULL
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
