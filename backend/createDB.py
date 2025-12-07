import sqlite3

database = "activity.db"

#initial table for primary functionality
def create_db():
    tables = [
        """CREATE TABLE IF NOT EXISTS activity_sessions(
                event_id INTEGER PRIMARY KEY AUTOINCREMENT,
                elapsed_time_in_minutes REAL NOT NULL,
                activity TEXT,
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
