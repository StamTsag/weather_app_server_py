import requests
import datetime
import random
import json

URL = "http://127.0.0.1:8000"
add_url = "{}/add_temp".format(URL)
add_last_url = "{}/add_last_temp".format(URL)

class Temp:
    y: int
    m: int
    d: int
    h: int
    averageTemp: str

now = datetime.datetime.now()
data = Temp()
data.y = now.year
data.m = now.month
data.d = now.day

def post_temp(url: str):
    requests.post(url, json.dumps(data.__dict__))

for i in range (0, 24):
    lower = random.uniform(21, 22.5)
    upper = random.uniform(22.5, 24.5)
    temp = random.uniform(lower, upper)
    data.averageTemp = str(round(temp, 2))
    data.h = i
    post_temp(add_url)

post_temp(add_last_url)
