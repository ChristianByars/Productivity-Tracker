import win32gui, win32process
import psutil
import time
from datetime import date
from add__activity import add_window, add_tab

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
    #these 2 variables help prevent consecutive logging
    prev_window, prev_tab = None, None

    #event__id = 1
    window_start_time = time.time()
    tab_start_time = time.time()
    todays_date = date.today()

    while True:
        hwnd, current_window = get_window()

        # track chrome tab
        if current_window == "chrome.exe" and hwnd:
            tab_name = win32gui.GetWindowText(hwnd)

            if tab_name != prev_tab:
                # Print time spent on previous tab
                end_time = time.time()
                elapsed = round(end_time - tab_start_time, 2)

                if prev_tab is not None:
                    print(f'{prev_tab} used for {elapsed} seconds')

                print(f'Chrome window: {tab_name}')

                # Update tab tracking
                tab_data = (elapsed, tab_name, todays_date)
                add_tab(tab_data)
                prev_tab = tab_name
                tab_start_time = time.time()

        # track application being used
        if current_window and current_window != prev_window:
            end_time = time.time()
            elapsed = round(end_time - window_start_time, 2)

            #track time on previous window
            if prev_window is not None:
                print(f'{prev_window} used for {elapsed} seconds')

            # Print new app
            session_data = (elapsed, current_window, todays_date)
            add_window(session_data)
            print(f'Current Application: {current_window}')

            # Update window tracking
            prev_window = current_window
            window_start_time = time.time()

            # Reset tab tracking if switching away from Chrome
            if current_window != "chrome.exe":
                prev_tab = None
                tab_start_time = time.time()    
        
store_window()



