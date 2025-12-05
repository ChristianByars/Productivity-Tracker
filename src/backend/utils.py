import sqlite3
import win32gui, win32process
import psutil

#this is for applications that are not google chrome
def log_window_data(activity):
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

def get_window():
    try:
        hwnd = win32gui.GetForegroundWindow()
        window_text = win32gui.GetWindowText(hwnd)
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        process = psutil.Process(pid)
        process_name = process.name()
        #return hwnd, process_name #save for later if/when I track YouTube usage
        #return process_name
        return window_text, process_name
    
    except Exception:
        return None, None

#this is for google chrome tracking
# def add_tab(tab):
#     database = "activity.db"
#     try:
#         with sqlite3.connect(database) as conn:
#             sql = """ INSERT INTO activity_sessions(
#             elapsed_time, 
#             app, 
#             browser_tab, 
#             date)
#               VALUES(?,?,?,?)"""
            
#             cur = conn.cursor()
#             cur.execute(sql, tab)

#             # commit the changes
#             conn.commit()
#     except sqlite3.OperationalError as e:
#         print(f'Error: {e}')
