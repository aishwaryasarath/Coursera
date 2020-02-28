

import requests
import socket


def check_localhost():
        localhost = socket.gethostbyname('localhost')
        return localhost=="127.0.0.1"
        # if localhost=="127.0.0.1":
        #         return True
        # else:
        #         return False


def check_connectivity():
        request = requests.get("http://www.google.com")
        return request.status_code == 200
        # if request.status_code == 200:
        #         print("True")
        #         return True
        # else:
        #         return False




check_localhost()
check_connectivity()

















