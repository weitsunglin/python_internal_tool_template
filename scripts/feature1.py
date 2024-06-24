# feature1.py

import datetime

def print_log():
    """
    Returns a log message with the current date and time.
    """
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"Log entry at {current_time}: This is a log message."
    return log_message
