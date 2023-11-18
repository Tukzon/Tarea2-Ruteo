import requests
import json

def get_accidentes_transito():
    url = "http://www.geoportal.cl/arcgis/rest/services/MinisteriodeTransporteyTelecomunicaciones/chile_mtt_conaset_accidente_pts_criticos_2019/MapServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"
    r = requests.get(url)
    data = json.loads(r.text)
    return data

print(get_accidentes_transito())