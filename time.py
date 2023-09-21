import json
import time
from urllib import request, response
import requests


while True:

    data={"altitude": 1000}
    x = requests.post("http://localhost:8027", json=data)
    if x.status_code==200:
        print("ok")
        print(x.json())
        time.sleep(3)


#print(x.json())