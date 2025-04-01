import requests
import json

URL = ""

def get_data():
    data = {}
    if id is not None:
        data = {'id':1}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(data)

get_data(1)