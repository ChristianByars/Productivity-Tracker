import sqlite3
import pywin, win32gui, win32process
import psutil

def get_window():
    try:
        hwnd = win32gui.GetForegroundWindow()
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        process = psutil.Process(pid)
        process_name = process.name()
        return hwnd, process_name
    
    except Exception:
        return None, None

def store_window():
    """These variables prevent program from constantly recording same tab
        and/or application"""
    prev_window, prev_tab = None, None

    while True:
        #get current window/application being used
        hwnd, current_window = get_window()
        
        #get google chrome tab
        if current_window == "chrome.exe" and hwnd:
            tab_name = win32gui.GetWindowText(hwnd)
            if tab_name != prev_tab:
                print(f'Chrome window: {tab_name}')
                prev_tab = tab_name

        #record current window
        if current_window and current_window != prev_window:
            print(f'Current Applcation: {current_window}')    
            prev_window = current_window
        
store_window()



