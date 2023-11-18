import requests
import json

# URL de la API https://api.xor.cl/red/bus-stop/{PA433} Parada de buses
url = "https://api.xor.cl/red/bus-stop/"

def get_info_paradero(id_paradero):
    response = requests.get(url + id_paradero)
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None