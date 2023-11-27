import requests

def obtener_datos_waze(api_key, latitud_inicio, longitud_inicio, latitud_final, longitud_final):
    url = "https://waze.p.rapidapi.com/alerts-and-jams"

    querystring = {
        "latStart": latitud_inicio,
        "lonStart": longitud_inicio,
        "latEnd": latitud_final,
        "lonEnd": longitud_final
    }

    headers = {
	"X-RapidAPI-Key": api_key,
	"X-RapidAPI-Host": "waze.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error en la solicitud: {response.status_code}"

# Usar la función
api_key = '6b8594f469msh1a559b7259e5fe2p1b8185jsn8951e0967107'
latitud_inicio = 'LATITUD_INICIO'
longitud_inicio = 'LONGITUD_INICIO'
latitud_final = 'LATITUD_FINAL'
longitud_final = 'LONGITUD_FINAL'

datos = obtener_datos_waze(api_key, latitud_inicio, longitud_inicio, latitud_final, longitud_final)
print(datos)
