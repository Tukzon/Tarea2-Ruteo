#!/bin/bash
set -e

# Instala PostGIS
apt-get update
apt-get install -y postgis postgresql-16-postgis-3

# Crear la extensión PostGIS en la base de datos predeterminada
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE EXTENSION IF NOT EXISTS postgis;
    CREATE EXTENSION IF NOT EXISTS postgis_topology;
EOSQL