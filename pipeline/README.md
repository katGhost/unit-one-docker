# DTC Zoomcamp: Data Engineering Homework 1

## Running the upload_data for taxi_zones:

uv run python upload_data.py \
  --pg-user=root \
  --pg-pass=root \
  --pg-host=localhost \
  --pg-port=5432 \
  --pg-db=ny_taxi \
  --target-table=taxi_zones


## Run the ingest_green_2025.py data:

uv run python ingest_green_2025.py \
  --pg-user=root \
  --pg-pass=root \
  --pg-host=localhost \
  --pg-port=5432 \
  --pg-db=ny_taxi \
  --target-table=green_taxi_trips_2025_11 \
  --year=2025 \
  --month=11 \
  --chunk_size=5000

## Question 3 query:

SELECT COUNT(*) AS trips_leq_mile
FROM green_taxi_trips_2025_11
WHERE trip_distance <= 1
AND lpep_pickup_datetime >= '2025-11-01'
AND lpep_pickup_datetime < '2025-12-01'

## Question 4 query:

SELECT
  DATE(lpep_pickup_datetime) AS pickup_day,
  MAX(trip_distance) AS max_trip_distance
FROM green_taxi_trips_2025_11
WHERE trip_distance < 100
GROUP BY pickup_day
ORDER BY max_trip_distance DESC;

## Question 5 query:

SELECT
  z.zone AS pickup_zone,
  SUM(g.total_amount) AS total_amount_sum
FROM green_taxi_trips_2025_11 g
JOIN taxi_zones z
  ON g.pulocationid = z."LocationID"
WHERE g.lpep_pickup_datetime >= '2025-11-18'
  AND g.lpep_pickup_datetime < '2025-11-19'
GROUP BY z.zone
ORDER BY total_amount_sum DESC
LIMIT 1;

## Question 6 query:

SELECT
  z_do.zone AS dropoff_zone,
  g.tip_amount,
  g.lpep_dropoff_datetime
FROM green_taxi_trips_2025_11 g
JOIN taxi_zones z_pu
  ON g."PULocationID" = z_pu."LocationID"
JOIN taxi_zones z_do
  ON g."DOLocationID" = z_do."LocationID"
WHERE z_pu.zone = 'East Harlem North'
  AND g.lpep_pickup_datetime >= '2025-11-01'
  AND g.lpep_pickup_datetime < '2025-12-01'
ORDER BY g.tip_amount DESC
LIMIT 1;



