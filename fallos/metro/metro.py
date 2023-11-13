import json
import requests

def get_metro_data():
    url = "https://api.xor.cl/red/metro-network"
    r = requests.get(url)
    data = json.loads(r.text)
    return data

print(get_metro_data())