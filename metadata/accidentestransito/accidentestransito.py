import requests
import json
import os

def get_accidentes_transito():
    #url = "http://www.geoportal.cl/arcgis/rest/services/MinisteriodeTransporteyTelecomunicaciones/chile_mtt_conaset_accidente_pts_criticos_2019/MapServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"
    url = "https://opendata.arcgis.com/api/v3/datasets/1f03237a14684ac280906f9ca6166d23_0/downloads/data?format=geojson&spatialRefId=4326&where=1=1"
    r = requests.get(url)
    data = json.loads(r.text)
    return data

def save_json(data):
    with open('./accidentes_transito.json', 'w') as file:
        json.dump(data, file)

save_json(get_accidentes_transito())