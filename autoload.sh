#!/bin/bash
echo "Añadiendo Plugins..."
psql -U postgres -d ruteo -h localhost -c "CREATE EXTENSION IF NOT EXISTS postgis;"
psql -U postgres -d ruteo -h localhost -c "CREATE EXTENSION IF NOT EXISTS postgis_raster;"
psql -U postgres -d ruteo -h localhost -c "CREATE EXTENSION IF NOT EXISTS pgrouting CASCADE;"
echo "Plugins añadidos exitosamente"
echo "Cargando datos de infraestructura..."
psql -U postgres -d ruteo -h localhost -f /infraestructura/gtfs_red/gtfs_tables.sql
echo "Cargando datos de GTFS..."
psql -U postgres -d ruteo -h localhost -f /infraestructura/gtfs_red/crear_shape.sql
echo "Cargando datos de GTFS..."
psql -U postgres -d ruteo -h localhost -f /infraestructura/gtfs_red/alimentar_gtfs.sql
echo "Cargando datos de GTFS..."
psql -U postgres -d ruteo -h localhost -f /infraestructura/gtfs_red/gtfs2rutas.sql
echo "Datos de GTFS cargados exitosamente"
echo "Cargando estaciones de metro..."
psql -U postgres -d ruteo -h localhost -f /infraestructura/EstacionesScript.sql
echo "Cargano mapa de metro..."
ogr2ogr -f "PostgreSQL" PG:"dbname=ruteo user=postgres password=ruteo host=localhost port=5432" /infraestructura/metro_mapa.geojson -nln metro_mapa -overwrite
echo "Infraestructura cargada exitosamente"
echo "Cargando metadata..."
ogr2ogr -f "PostgreSQL" PG:"dbname=ruteo user=postgres password=ruteo host=localhost port=5432" /metadata/accidentestransito/accidentes_transito.json -nln accidentes_transito -overwrite
echo "Accidentes de tránsito cargados exitosamente"
ogr2ogr -f "PostgreSQL" PG:"dbname=ruteo user=postgres password=ruteo host=localhost port=5432" /metadata/stop/images/hexagonos_radial.geojson -nln stop -overwrite
echo "Datos de robos cargados exitosamente"
