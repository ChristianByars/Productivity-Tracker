import sqlite3
import win32gui, win32process
import psutil
from .config import PROCESS_PATTERNS

#log data into SQL database
def log_data(activity):
    database = "activity.db"
    try:
        with sqlite3.connect(database) as conn:
            sql = """ INSERT INTO activity_sessions(
            elapsed_time_in_minutes, 
            activity,
            date)
              VALUES(?,?,?)"""
            
            cur = conn.cursor()
            cur.execute(sql, activity)

            # commit the changes
            conn.commit()
    except sqlite3.OperationalError as e:
        print(f'Error: {e}')
        

#obtain executable and window text
def get_window():
    try:
        hwnd = win32gui.GetForegroundWindow()
        window_text = win32gui.GetWindowText(hwnd)
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        process = psutil.Process(pid)
        process_name = process.name()
        return window_text, process_name
    
    except Exception:
        return None, None
    

def extract_window_text(process_name, window_title):
    #base cases
    if process_name is None: return False
    if window_title is None or window_title == "": return False
    
    process = process_name.lower()
    #title = window_title.lower()
    
   
    # 1. PROCESS-NAME PATTERNS
    for category, patterns in PROCESS_PATTERNS.items():
        #check for patterns and then decide if you use process or window text
        if any(p in process for p in patterns):

            # Categories where window text is needed:
            if category in ["browsers", "office_apps"]:
                return True

            # Categories where window text isn't needed:
            if category in ["system_apps", "communication_apps", "code_editors"]:
                return False

    # # Blank or useless titles
    # if not title or title.strip() == "":
    #     return False
    
    #if app isn't in config, just obtain the window text
    return True
