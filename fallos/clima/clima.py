import requests


def obtener_condiciones_climaticas(api_key, location_key):
    # URL de la API para condiciones actuales
    url = f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}"

    # Parámetros de consulta, incluyendo tu clave API
    params = {
        'apikey': api_key,
        'language': 'es-es',  # Cambia el lenguaje aquí si es necesario
        'details': 'false'    # Cambia a 'true' si necesitas más detalles
    }

    # Realizar la solicitud a la API
    response = requests.get(url, params=params)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error en la solicitud: {response.status_code}"


def obtener_location_key(api_key, latitud, longitud):
    # URL de la API para buscar por coordenadas geográficas
    url = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search"

    # Parámetros de consulta
    params = {
        'apikey': api_key,
        'q': f"{latitud},{longitud}",
        'language': 'es-es'  # Cambia el lenguaje aquí si es necesario
    }

    # Realizar la solicitud a la API
    response = requests.get(url, params=params)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        data = response.json()
        return data.get('Key')
    else:
        return f"Error en la solicitud: {response.status_code}"

# Usar la función
api_key = 'YyAnoNNyAfjzO4QgNtXwntcnA93Qd3jd '
latitud = '40.7128'  # Ejemplo de latitud
longitud = '-74.0060'  # Ejemplo de longitud

location_key = obtener_location_key(api_key, latitud, longitud)
print(location_key)

condiciones = obtener_condiciones_climaticas(api_key, location_key)
print(condiciones)
