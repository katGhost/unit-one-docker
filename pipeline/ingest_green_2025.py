#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
from tqdm import tqdm
import click
import numpy as np

# Data parsing
dtype_backend = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]


@click.command()
@click.option('--pg-user', default='root')
@click.option('--pg-pass', default='root')
@click.option('--pg-host', default='pgdatabase')
@click.option('--pg-port', default=5432)
@click.option('--pg-db', default='ny_taxi')
@click.option('--year', type=int, default=2025)
@click.option('--month', type=int, default=1)
@click.option('--target-table', default='yellow_taxi_trips')
@click.option('--chunk_size', type=int, default=5000, help='Chunk_size for ingestion')
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, year, month, chunk_size, target_table):

    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    prefix = ("https://d37ci6vzurychx.cloudfront.net/trip-data/")
    url =f"{prefix}green_tripdata_{year}-{month:02d}.parquet"

    print(f"Downloading {url}")

    df = pd.read_parquet(
        url,
        engine='pyarrow',
    )

    #print(f"Reading parquet file: {url}")

    print(f"Rows: {len(df)}")
    #print("Columns:", df.columns.tolist())

    df.columns = [c.lower() for c in df.columns]
    chunks = np.array_split(df, (len(df) // chunk_size) + 1)
    first = True
    for df_chunk in tqdm(chunks):

        if first:
            df_chunk.to_sql(
                name=target_table,
                con=engine,
                if_exists="replace"
            )
            first = False

        # Insert chunk
        df_chunk.to_sql(
            name=target_table,
            con=engine,
            if_exists="append"
        )

    print(f"Ingested {len(df)} into {target_table}")


if __name__ == '__main__':
    run()
