COPY calendar(service_id,monday,tuesday,wednesday,thursday,friday,saturday,sunday,start_date,end_date) 
FROM 'C:\Users\Paolo\AppData\Roaming\DBeaverData\workspace6\General\Scripts\gtfs_red\calendar.txt' DELIMITER ',' CSV HEADER;
COPY calendar_dates(service_id,date,exception_type)
FROM 'C:\Users\Paolo\AppData\Roaming\DBeaverData\workspace6\General\Scripts\gtfs_red\calendar_dates.txt' DELIMITER ',' CSV HEADER;
COPY stop_times(trip_id,arrival_time,departure_time,stop_id,stop_sequence) 
FROM 'C:\Users\Paolo\AppData\Roaming\DBeaverData\workspace6\General\Scripts\gtfs_red\stop_times.txt' DELIMITER ','
CSV HEADER;
COPY trips(route_id,service_id,trip_id,trip_headsign,direction_id,shape_id)
FROM 'C:\Users\Paolo\AppData\Roaming\DBeaverData\workspace6\General\Scripts\gtfs_red\trips.txt' DELIMITER ',' CSV HEADER;
COPY agency(agency_id,agency_name,agency_url,agency_timezone)
FROM 'C:\Users\Paolo\AppData\Roaming\DBeaverData\workspace6\General\Scripts\gtfs_red\agency.txt' DELIMITER ',' CSV HEADER;
COPY routes(route_id,agency_id,route_short_name,route_long_name,route_desc,route_type,route_url,route_color,route_text_color) 
FROM 'C:\Users\Paolo\AppData\Roaming\DBeaverData\workspace6\General\Scripts\gtfs_red\routes.txt' DELIMITER ','
CSV HEADER;
COPY shapes(shape_id,shape_pt_lat,shape_pt_lon,shape_pt_sequence)
FROM 'C:\Users\Paolo\AppData\Roaming\DBeaverData\workspace6\General\Scripts\gtfs_red\hapes.txt' DELIMITER ',' CSV HEADER;
COPY stops(stop_id,stop_code,stop_name,stop_lat,stop_lon,stop_url,wheelchair_boarding) 
FROM 'C:\Users\Paolo\AppData\Roaming\DBeaverData\workspace6\General\Scripts\gtfs_red\stops.txt' DELIMITER ','
CSV HEADER;
COPY feed_info(feed_publisher_name,feed_publisher_url,feed_lang,feed_start_date,feed_end_date,feed_version) 
FROM 'C:\Users\Paolo\AppData\Roaming\DBeaverData\workspace6\General\Scripts\gtfs_red\feed_info.txt' DELIMITER ','
CSV HEADER;
COPY frequencies(trip_id,start_time,end_time,headway_secs,exact_times) 
FROM 'C:\Users\Paolo\AppData\Roaming\DBeaverData\workspace6\General\Scripts\gtfs_red\requencies.txt' DELIMITER ','
CSV HEADER