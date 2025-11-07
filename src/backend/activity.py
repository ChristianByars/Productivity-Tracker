import sqlite3
import pywin, win32gui, win32process
import psutil
from win32com.client import GetObject
import time

def get_window():
    prev_window=None
    while True:
        current_window = win32gui.GetForegroundWindow()
        time.sleep(3)
        try:
            _,pid = win32process.GetWindowThreadProcessId(current_window)
            process = psutil.Process(pid)
            process_name = process.name()

            if process_name != prev_window and process_name != "explorer.exe":
                print(f'Current Applcation: {process_name}')
                prev_window=process_name
                
        except:
            print("Couldn't get the process id")
        

get_window()



