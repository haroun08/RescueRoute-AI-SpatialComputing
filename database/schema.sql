CREATE EXTENSION postgis;

CREATE TABLE traffic_data (
    id SERIAL PRIMARY KEY,
    location GEOMETRY(Point, 4326),
    timestamp TIMESTAMP,
    traffic_level INT
);

CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    location GEOMETRY(Point, 4326),
    timestamp TIMESTAMP,
    weather_condition VARCHAR(50),
    impact VARCHAR(50)
);