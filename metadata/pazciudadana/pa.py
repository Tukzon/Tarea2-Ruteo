import requests
import pandas as pd
import json
import os
from unidecode import unidecode

def eliminar_tildes(texto):
    return unidecode(texto) if isinstance(texto, str) else texto

def limpiar_texto(texto):
    if isinstance(texto, str):
        texto = eliminar_tildes(texto)
        texto = texto.replace('\\', '')  # Eliminar backslashes
        # Aquí puedes añadir más reemplazos o limpieza según necesites
    return texto

# URL de la solicitud

url = "https://datoscomunales.pazciudadana.cl/excel?t=2023-04-01&q=casospoliciales&f=quarter"

# Encabezados personalizados
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': 'laravel_session=eyJpdiI6ImVodEdcL1VcL3dFZHc3Rmd0cEp1VnFXbmVyUjhlaVFRMG1uTlBMSXZxeFVvcz0iLCJ2YWx1ZSI6InhNS1RTTG03djVBR1VWMTBITmZkUmZSQnRjcnhldlcrNFVaNmpoSzB1XC9ZSHV6STJOQklFTkdJMEs4RnY2UE5JOTgzWFI2MHl6TGxQd2hKRFpKSm52QT09IiwibWFjIjoiNmFjYzBiMTE2MGMzMDlhNjBkMmQ2YzI4NGE3NGNhY2I0MDI1YWFmN2I0YzI4M2M0YTc4YzA0ZGZjNjUyNmUzZSJ9',
    'If-Modified-Since': 'Sun, 26 Nov 2023 04:13:34 GMT',
    'Referer': 'https://datoscomunales.pazciudadana.cl/',
    'Sec-Ch-Ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

# Realizar la solicitud GET
response = requests.get(url, headers=headers)

# Verificar el estado de la respuesta
if response.status_code == 200:
    # Guardar el contenido en un archivo
    with open("data/pazciudadana.xlsx", 'wb') as f:
        f.write(response.content)
    print("Archivo descargado con éxito.")
else:
    print("Error en la solicitud:", response.status_code)


def read_data_to_json(file_path):
    excel_data = pd.ExcelFile(file_path, engine='openpyxl')
    data_df = pd.read_excel(excel_data, sheet_name=0, header=6)
    
    cleaned_data_df = data_df.drop(data_df.index[0]).reset_index(drop=True)
    
    cleaned_data_df.columns = ['Tipo de Información', 'Comuna', 'Frecuencia', 'Tasa cada 100Mil', 'Rango']

    for columna in cleaned_data_df.columns:
        cleaned_data_df[columna] = cleaned_data_df[columna].apply(limpiar_texto)
        cleaned_data_df[columna] = cleaned_data_df[columna].apply(eliminar_tildes)
        
    
    cleaned_data_df = cleaned_data_df.drop(columns=['Tipo de Información'])
    
    json_data = cleaned_data_df.to_json(orient='records')
    
    return json_data


respuesta = read_data_to_json("data/pazciudadana.xlsx")

def save_json(data):
    with open('./paz.json', 'w') as file:
        json.dump(json.loads(data), file)

save_json(respuesta)