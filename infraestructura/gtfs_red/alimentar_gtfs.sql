COPY calendar(service_id,monday,tuesday,wednesday,thursday,friday,saturday,sunday,start_date,end_date) 
FROM '/infraestructura/gtfs_red/calendar.txt' DELIMITER ',' CSV HEADER;
COPY calendar_dates(service_id,date,exception_type)
FROM '/infraestructura/gtfs_red/calendar_dates.txt' DELIMITER ',' CSV HEADER;
COPY stop_times(trip_id,arrival_time,departure_time,stop_id,stop_sequence) 
FROM '/infraestructura/gtfs_red/stop_times.txt' DELIMITER ','
CSV HEADER;
COPY trips(route_id,service_id,trip_id,trip_headsign,direction_id,shape_id)
FROM '/infraestructura/gtfs_red/trips.txt' DELIMITER ',' CSV HEADER;
COPY agency(agency_id,agency_name,agency_url,agency_timezone)
FROM '/infraestructura/gtfs_red/agency.txt' DELIMITER ',' CSV HEADER;
COPY routes(route_id,agency_id,route_short_name,route_long_name,route_desc,route_type,route_url,route_color,route_text_color) 
FROM '/infraestructura/gtfs_red/routes.txt' DELIMITER ','
CSV HEADER;
COPY shapes(shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence)
FROM '/infraestructura/gtfs_red/shapes.txt' DELIMITER ',' CSV HEADER;
COPY stops(stop_id,stop_code,stop_name,stop_lat,stop_lon,stop_url,wheelchair_boarding) 
FROM '/infraestructura/gtfs_red/stops.txt' DELIMITER ','
CSV HEADER;
COPY feed_info(feed_publisher_name,feed_publisher_url,feed_lang,feed_start_date,feed_end_date,feed_version) 
FROM '/infraestructura/gtfs_red/feed_info.txt' DELIMITER ','
CSV HEADER;
COPY frequencies(trip_id,start_time,end_time,headway_secs,exact_times) 
FROM '/infraestructura/gtfs_red/frequencies.txt' DELIMITER ','
CSV HEADER