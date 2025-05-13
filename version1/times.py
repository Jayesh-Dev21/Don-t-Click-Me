import time
from datetime import datetime

def get_current_time():
    """
    This function returns the current time in HH:MM:SS format.
    """
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")  
    return current_time



