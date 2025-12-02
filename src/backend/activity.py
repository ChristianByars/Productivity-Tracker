import sqlite3
import pywin, win32gui, win32process
import psutil
import time

def get_window():
    try:
        current_window = win32gui.GetForegroundWindow()

        """give your system time to obtain the next window. If you don't sleep,
            your computer will not be able to accurately track your windows"""
        time.sleep(2)

        _,pid = win32process.GetWindowThreadProcessId(current_window)
        process = psutil.Process(pid)
        process_name = process.name()  
        return current_window, process_name
        
    except Exception:
        return None, None

def store_window():
    prev_window = None
    prev_tab, tab_name = None, None
    while True:
        #get current window/application being used
        tab, current_window = get_window()
        tab_name = win32gui.GetWindowText(tab)
        
        if tab_name and tab_name != prev_tab:
            #tab_name = win32gui.GetWindowText(tab)
            print(f'Chrome window: {tab_name}')
            prev_tab = tab_name

        if current_window and current_window != prev_window:
            print(f'Current Applcation: {current_window}')    
            prev_window = current_window
        
store_window()



