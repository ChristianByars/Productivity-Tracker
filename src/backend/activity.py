import time
from datetime import date
from utils import log_window_data, get_window

def store_window():
    #this variable help prevent consecutive logging
    prev_window = None

    window_start_time = time.time()
    todays_date = date.today()

    while True:
        #hwnd, process_name = get_window() #save for if/when I track YouTube usage
        window_text, process_name = get_window()
        # track application being used
        if process_name and process_name != prev_window:
            end_time = time.time()
            elapsed_time = round(end_time - window_start_time, 2)


            #print(f'Current Application: {process_name}')

            # store window data before switching
            if elapsed_time > 3:
                print(f'You spent {elapsed_time} on {window_text}') #for debugging
                print()
                session_data = (elapsed_time, process_name, todays_date)
                #log_window_data(session_data)
    
            # Update window tracking
            prev_window = process_name
            window_start_time = time.time() 
        
store_window()



