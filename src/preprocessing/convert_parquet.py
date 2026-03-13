"""ETL script: convert clean-non-market-housing.csv to Parquet.

Adapted from lecture notes.

Run with the following command from the root directory:
    python src/preprocessing/convert_parquet.py
"""
import duckdb

CSV = "data/processed/clean-non-market-housing.csv"
OUT = "data/processed/clean-non-market-housing.parquet"

duckdb.execute(f"""
    COPY (SELECT * EXCLUDE ("column00") FROM read_csv_auto('{CSV}'))
    TO '{OUT}' (FORMAT PARQUET)
""")