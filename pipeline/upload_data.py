#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
import click

@click.command()
@click.option('--pg-user', default='root')
@click.option('--pg-pass', default='root')
@click.option('--pg-host', default='localhost')
@click.option('--pg-port', default=5432)
@click.option('--pg-db', default='ny_taxi')
@click.option('--target-table', default='taxi_zones')
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, target_table):

    engine = create_engine(
        f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}'
    )

    url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"

    df = pd.read_csv(url)

    # Normalize column names
    df.columns = [c.lower() for c in df.columns]

    df.to_sql(
        name=target_table,
        con=engine,
        if_exists='replace',
        index=False
    )

    print(f"Loaded {len(df)} rows into {target_table}")

if __name__ == '__main__':
    run()
