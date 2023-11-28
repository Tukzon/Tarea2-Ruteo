-- Create a table to store the shape geometries
DROP TABLE IF EXISTS shape_geoms CASCADE;
CREATE TABLE shape_geoms (
  shape_id TEXT NOT NULL,
  shape_geom GEOMETRY('LINESTRING', 4326),
  CONSTRAINT shape_geom_pkey PRIMARY KEY (shape_id)
);

-- Drop the index if it exists
DROP INDEX IF EXISTS shape_geoms_key;

-- Create an index on the shapes table for the shape_id column
CREATE INDEX shape_geoms_key ON shapes (shape_id);
