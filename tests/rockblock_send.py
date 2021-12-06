import requests
import json
import time
import random


url = 'http://localhost:8080/'

headers = {
       'content-type': 'application/json',
       'accept': 'application/json'
}


while True:
       data = {
              "imei": "300234063233380",
              "serial": 9068,
              "momsn": 669,
              "transmit_time": "21-12-06 10:35:52",
              "iridium_latitude": 31.4741,
              "iridium_longitude": 144.5242,
              "iridium_cep": 108,
              "data": f"{dict(token='my-token', temperature=20+random.random())}".encode().hex()
       }

       r = requests.post(url, headers=headers, data=json.dumps(data))
       print(r.json())

       time.sleep(5)
