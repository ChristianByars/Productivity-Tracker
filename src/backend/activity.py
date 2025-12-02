import sqlite3
import pywin, win32gui, win32process
import psutil
import time

def get_window():
    prev_window = None
    prev_tab = None
    while True:
        current_window = win32gui.GetForegroundWindow()
        time.sleep(3)
        try:
            _,pid = win32process.GetWindowThreadProcessId(current_window)
            process = psutil.Process(pid)
            process_name = process.name()
            tab_name = win32gui.GetWindowText(current_window)
            
            if process_name == "chrome.exe" and tab_name != prev_tab:
                print(f'Chrome window: {tab_name}')
                prev_tab = tab_name
            
            if process_name != prev_window:
                print(f'Current Applcation: {process_name}')    
                prev_window=process_name
                
                
        except:
            print("Couldn't get the process id")
        

get_window()



