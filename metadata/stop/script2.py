import rasterio
import numpy as np
import json
from shapely.geometry import shape, Polygon, Point
import cv2

# Carga y procesamiento del GeoTIFF
with rasterio.open("./images/stop-Robos-4k.tif") as src:
    raster_data = src.read()
    raster_transform = src.transform
    raster_width, raster_height = src.width, src.height

# Función para detectar hexágonos y calcular centroides (esta parte es hipotética y debe ser implementada)
def detect_hexagons_and_calculate_centroids(raster_data, transform):
    # Esta función debería implementar un algoritmo de detección de formas para encontrar hexágonos
    # en raster_data y calcular sus centroides. Este es un enfoque hipotético.
    detected_hexagons = []  # Aquí se almacenarían los contornos de los hexágonos detectados
    centroids = []

    for hexagon in detected_hexagons:
        # Calcular el centroide del hexágono
        M = cv2.moments(hexagon)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            # Convertir coordenadas de píxeles a coordenadas geoespaciales
            geo_x, geo_y = transform * (cx, cy)
            centroids.append((geo_x, geo_y))

    return centroids

# Detectar hexágonos y obtener centroides
hexagon_centroids = detect_hexagons_and_calculate_centroids(raster_data, raster_transform)

# Convertir centroides a GeoJSON
geojson_features = [{
    "type": "Feature",
    "geometry": {
        "type": "Point",
        "coordinates": [centroid[0], centroid[1]]
    },
    "properties": {}
} for centroid in hexagon_centroids]

geojson_structure = {
    "type": "FeatureCollection",
    "features": geojson_features
}

# Guardar los centroides como GeoJSON
geojson_centroids_path = ".images/geotiff_centroids.geojson"
with open(geojson_centroids_path, 'w') as f:
    json.dump(geojson_structure, f)

# Conversión de puntos a hexágonos
def convert_points_to_hexagons(features, hexagon_area):
    # Calcula la longitud del lado del hexágono basada en el área
    hexagon_side_length = np.sqrt((2 * hexagon_area) / (3 * np.sqrt(3)))

    hexagons = []
    for feature in features:
        center = feature["geometry"]["coordinates"]
        hexagon = []
        for angle in range(0, 360, 60):
            x = center[0] + np.cos(np.radians(angle)) * hexagon_side_length
            y = center[1] + np.sin(np.radians(angle)) * hexagon_side_length
            hexagon.append((x, y))
        hexagons.append({
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [hexagon + [hexagon[0]]]  # Cerrar el polígono
            },
            "properties": feature["properties"]
        })

    return hexagons

# Tamaño del hexágono (este valor debe ser ajustado adecuadamente)
hexagon_size = 770  # Ejemplo de tamaño, ajusta según tus necesidades

# Convertir puntos a hexágonos
hexagon_features = convert_points_to_hexagons(geojson_features, hexagon_size)

# Asignar pesos radiales
santiago_center = Point(-70.64827, -33.45694)  # Coordenadas de Santiago Centro

def assign_radial_weights(features, center):
    for feature in features:
        geom = shape(feature['geometry'])
        distance = geom.distance(center)
        if distance < 0.05:  # Central Santiago
            feature['properties']['weight'] = 3
        elif distance < 0.1:  # Comunas circundantes
            feature['properties']['weight'] = 2
        else:  # Más lejos
            feature['properties']['weight'] = 1

# Asignar pesos
assign_radial_weights(hexagon_features, santiago_center)

# Guardar hexágonos con pesos
geojson_hexagons_path = "./images/geojson_hexagons.geojson"
with open(geojson_hexagons_path, 'w') as f:
    json.dump({"type": "FeatureCollection", "features": hexagon_features}, f)
