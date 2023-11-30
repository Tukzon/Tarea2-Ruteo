import requests
import pandas as pd
import json

# URL de la solicitud
url = "https://datoscomunales.pazciudadana.cl/excel?t=2023-04-01&q=denuncias&f=quarter"

# Encabezados personalizados
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cookie': 'gid=GA1.2.2094129065.1700963169; _gcl_au=1.1.1817751939.1700968661; laravel_session=eyJpdiI6ImdhV0RvNm44UFlDUHRweUkxZkFBcEd2UWc5REJIY1lPNGRyUHM1NTNUMkk9IiwidmFsdWUiOiJ5cWhiVnJ1NDdMZmNZdlwvOGo0QWFQNDNUWVNWa2JWSURjUEc2eFUyXC8raVNYajlLbDYzMFwvM1ZYT3dsSFZmcVFHWndubmtTMTZ6WWVOUUFGZWdyUnN6Zz09IiwibWFjIjoiYTM0NzEwNTVkMmU3NDhiZTFhZDdlOGFhZTEyYTQ3N2IyMDA3OGY4NjAxOTFjNTRmMDIxM2JlZmQxM2FmY2RlYyJ9; _ga_XJPWCEHCEV=GS1.1.1701027061.4.1.1701027061.0.0.0; _gat_gtag_UA_77866860_1=1; _ga=GA1.1.995760676.1700963169; _ga_D2ZEK0HR6G=GS1.1.1701029710.3.0.1701029713.0.0.0',
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
    
    cleaned_data_df = cleaned_data_df.drop(columns=['Tipo de Información'])
    
    json_data = cleaned_data_df.to_json(orient='records')
    
    return json_data


respuesta = read_data_to_json("data/pazciudadana.xlsx")