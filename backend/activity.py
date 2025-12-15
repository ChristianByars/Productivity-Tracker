import time
from datetime import date
from .utils import log_data, get_window, extract_window_text
from .config import MIN_DURATION_IN_SECONDS

def run_tracker():
    # Track previous session label AND raw window/ process state
    session_to_log = None
    current_activity = None

    window_start_time = time.time()
    todays_date = date.today()
    
    print("Tracker Running")

    while True:
        window_text, process_name = get_window()

        #make sure process name exists
        if process_name is None: continue
        if window_text == "": continue

        use_title = extract_window_text(process_name, window_text)

        # Decide activity label
        if use_title:
            current_activity = window_text
        else:
            current_activity = process_name

        #keep track of session changes
        session_changed = False
             
        if current_activity != session_to_log:
            session_changed = True
         
        """This will run on the first iteration but will not be stored into the database due to the minimum
        threshold. After the first iteration, sessions will be logged if they hit the minimum threshold AND
        when you move into a new window and/or tab. """
        
        if session_changed:
            end_time = time.time()
            elapsed_time = round(end_time - window_start_time, 2)
            
            #log data
            if elapsed_time > MIN_DURATION_IN_SECONDS:
                #store elapsed time as minutes in database
                session = (round(elapsed_time/60, 2), session_to_log, todays_date)
                log_data(session)

                # print(f'Session Logged: {session_to_log}, time in minutes: {elapsed_time/60}')

                # print(f'New Session: {current_activity}\n')
            
            # keep track of previous session
            session_to_log = current_activity
            window_start_time = time.time()

