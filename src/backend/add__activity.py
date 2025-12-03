import sqlite3

def add_window(activity):
    database = "activity.db"
    try:
        with sqlite3.connect(database) as conn:
            sql = """ INSERT INTO activity_sessions(
            elapsed_time, 
            app, 
            browser_tab, 
            date)
              VALUES(?,?,NULL,?)"""
            
            cur = conn.cursor()
            cur.execute(sql, activity)

            # commit the changes
            conn.commit()
    except sqlite3.OperationalError as e:
        print(f'Error: {e}')



def add_tab(tab):
    database = "activity.db"
    try:
        with sqlite3.connect(database) as conn:
            sql = """ INSERT INTO activity_sessions(
            elapsed_time, 
            app, 
            browser_tab, 
            date)
              VALUES(?,NULL,?,?)"""
            
            cur = conn.cursor()
            cur.execute(sql, tab)

            # commit the changes
            conn.commit()
    except sqlite3.OperationalError as e:
        print(f'Error: {e}')
