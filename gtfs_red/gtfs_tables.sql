-- Drops existing tables if they exist
DROP TABLE IF EXISTS trips CASCADE;
DROP TABLE IF EXISTS stop_times CASCADE;
DROP TABLE IF EXISTS frequencies CASCADE;
DROP TABLE IF EXISTS routes CASCADE;
DROP TABLE IF EXISTS shapes CASCADE;
DROP TABLE IF EXISTS calendar CASCADE;
DROP TABLE IF EXISTS stops CASCADE;
DROP TABLE IF EXISTS agency CASCADE;
DROP TABLE IF EXISTS calendar_dates CASCADE;
DROP TABLE IF EXISTS feed_info CASCADE;

-- Create table for trips
CREATE TABLE trips (
    route_id VARCHAR(255),
    service_id VARCHAR(255),
    trip_id VARCHAR(255) PRIMARY KEY,
    trip_headsign VARCHAR(255),
    direction_id INTEGER,
    shape_id VARCHAR(255)
);

-- Create table for stop_times
CREATE TABLE stop_times (
    trip_id VARCHAR(255),
    arrival_time TIME,
    departure_time TIME,
    stop_id VARCHAR(255),
    stop_sequence INTEGER
);

-- Create table for frequencies
CREATE TABLE frequencies (
    trip_id VARCHAR(255),
    start_time TIME,
    end_time TIME,
    headway_secs INTEGER,
    exact_times INTEGER
);

-- Create table for routes
CREATE TABLE routes (
    route_id VARCHAR(255) PRIMARY KEY,
    agency_id VARCHAR(255),
    route_short_name VARCHAR(255),
    route_long_name VARCHAR(255),
    route_desc TEXT,
    route_type INTEGER,
    route_url VARCHAR(255),
    route_color VARCHAR(7),
    route_text_color VARCHAR(7)
);

-- Create table for shapes
CREATE TABLE shapes (
    shape_id VARCHAR(255),
    shape_pt_lat DECIMAL(10, 7),
    shape_pt_lon DECIMAL(10, 7),
    shape_pt_sequence INTEGER
);

-- Create table for calendar
CREATE TABLE calendar (
    service_id VARCHAR(255) PRIMARY KEY,
    monday INTEGER,
    tuesday INTEGER,
    wednesday INTEGER,
    thursday INTEGER,
    friday INTEGER,
    saturday INTEGER,
    sunday INTEGER,
    start_date DATE,
    end_date DATE
);

-- Create table for stops
CREATE TABLE stops (
    stop_id VARCHAR(255) PRIMARY KEY,
    stop_code VARCHAR(255),
    stop_name VARCHAR(255),
    stop_lat DECIMAL(10, 7),
    stop_lon DECIMAL(10, 7),
    stop_url VARCHAR(255),
    wheelchair_boarding INTEGER,
    stop_geom geometry('POINT', 4326)
);

-- Create table for agency
CREATE TABLE agency (
    agency_id VARCHAR(255) PRIMARY KEY,
    agency_name VARCHAR(255),
    agency_url VARCHAR(255),
    agency_timezone VARCHAR(255)
);

-- Create table for calendar_dates
CREATE TABLE calendar_dates (
    service_id VARCHAR(255),
    date DATE,
    exception_type INTEGER
);

-- Create table for feed_info
CREATE TABLE feed_info (
    feed_publisher_name VARCHAR(255),
    feed_publisher_url VARCHAR(255),
    feed_lang VARCHAR(255),
    feed_start_date DATE,
    feed_end_date DATE,
    feed_version VARCHAR(255)
);
