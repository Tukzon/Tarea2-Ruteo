import cv2
import rasterio
from rasterio.features import shapes
from shapely.geometry import shape, Polygon
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt

# Función para convertir HEX a escala de grises (simplificación para la demostración)
def hex_to_gray(hex_color):
    hex_color = hex_color.lstrip('#')
    return sum(int(hex_color[i:i+2], 16) for i in (0, 2, 4)) // 3

# Colores hexadecimales de los hexágonos y sus bordes (en gris para simplificar)
#hex_colors = [hex_to_gray(c) for c in ['#FDE589', '#FDD7A9', '#FDC9C9']]
hex_colors = ['#FDE589', '#FDD7A9', '#FDC9C9']
#border_colors = [hex_to_gray(c) for c in ['#FBBF24', '#FF923E', '#F97474']]

# Cargar la imagen GeoTIFF con rasterio
with rasterio.open('./images/stop-Robos-4k.tif') as src:
    img = src.read(1)  # Leer la primera banda (asumiendo que es una imagen de una banda)
    plt.imshow(img, cmap='gray')
    plt.title('Imagen Original')
    plt.show()
    transform = src.transform  # Obtener la transformación afín
    crs = src.crs  # Sistema de referencia de coordenadas

block_size = 51
C = 1

adaptive_thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, block_size, C)
plt.imshow(adaptive_thresh, cmap='gray')
plt.title('Umbral Adaptativo')
plt.show()

contours, _ = cv2.findContours(adaptive_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

hexagon_contours = []
for contour in contours:
    # Calcular el área del contorno
    area = cv2.contourArea(contour)

    # Aproximar la forma del contorno basándonos en el perímetro
    perimeter = cv2.arcLength(contour, True)
    epsilon = 0.025 * perimeter  # El valor 0.025 es un valor inicial, ajusta según sea necesario
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # Asumir que los hexágonos tienen 6 lados, pero ajusta según sea necesario
    if len(approx) == 6 and 500 < area < 1000:
        hexagon_contours.append(approx)

contour_img = cv2.drawContours(np.zeros_like(img), hexagon_contours, -1, (255,0,0), 1)
plt.imshow(contour_img)
plt.title('Contornos de Hexágonos')
plt.show()

hexagon_geometries = []
for contour in hexagon_contours:
    # Obtener la forma geométrica del contorno
    geom = shapes(adaptive_thresh.astype(np.int16), mask=None, transform=transform).__next__()[0]
    polygon = shape(geom)
    hexagon_geometries.append(polygon)

# Asegurarse de que hay geometrías en la lista antes de crear el GeoDataFrame
if not hexagon_geometries:
    raise ValueError("No se crearon geometrías. Los contornos pueden no corresponder a hexágonos.")

# Crear un GeoDataFrame con las geometrías de los hexágonos
gdf = gpd.GeoDataFrame({'geometry': hexagon_geometries}, crs=crs.to_dict())

# Guardar el GeoDataFrame en un archivo shapefile para verificación
gdf.to_file("hexagons.shp", driver='ESRI Shapefile')

# Conectar a la base de datos PostGIS y exportar
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:ruteo@localhost:5432/ruteo')
gdf.to_postgis(name='hexagonos', con=engine, if_exists='replace', index=False)