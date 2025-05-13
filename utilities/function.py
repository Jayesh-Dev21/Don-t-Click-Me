import random
import os
import socket
from utilities.text_dialoge import phrases
from utilities.time_info import get_current_time
import requests
from utilities.user import send_data, local_user
from utilities.ip_addr import get_ip




def print_time():
    return get_current_time()

def randomize(n, m):
    
    if n <= 0:
        raise ValueError("n must be a positive integer")
    return random.randint(m, n)

def on_click():
    # print("You clicked the button!")
    # user_details()
    send_data(local_user)
    return "You clicked the button!"


def user_details():
    print("User details:")
    try:
        print(f"User ID: {os.getuid()}")
    except AttributeError:
        print("User ID: Not available on this OS (likely Windows)")

    try:
        print(f"User Name: {os.getlogin()}")
    except Exception:
        # Fallback for systems where os.getlogin() might fail
        import getpass
        print(f"User Name: {getpass.getuser()}")

    print(f"User Home Directory: {os.path.expanduser('~')}")
    
    # Get IP address

    print(f"Your IP Address is: {get_ip()}")
    return



def phrase(n):
    return phrases[n]


def prompt(n):
 return phrase(39 - n)