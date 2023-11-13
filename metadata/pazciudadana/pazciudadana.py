import requests
import pandas as pd
import json

def download_latest_excel_santiago():
    url = "https://datoscomunales.pazciudadana.cl/excel?t=2023-01-01&q=casospoliciales&f=quarter"
    r = requests.get(url)
    with open("./data/pazciudadana.xlsx", 'wb') as f:
        f.write(r.content)

def read_data_to_json(file_path):
    excel_data = pd.ExcelFile(file_path, engine='openpyxl')
    data_df = pd.read_excel(excel_data, sheet_name=0, header=6)
    
    cleaned_data_df = data_df.drop(data_df.index[0]).reset_index(drop=True)
    
    cleaned_data_df.columns = ['Tipo de Información', 'Comuna', 'Frecuencia', 'Tasa cada 100Mil', 'Rango']
    
    cleaned_data_df = cleaned_data_df.drop(columns=['Tipo de Información'])
    
    json_data = cleaned_data_df.to_json(orient='records')
    
    return json_data