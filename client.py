import json
import time
from urllib import request, response
import requests


import requests

pxdata = ('Version', 14)

while True:

    data={"altitude": 1000}
    x = requests.post("http://localhost:8027", json=data)
    if x.status_code==200:
        print(x.json())
        print("ok")
        time.sleep(1)

