"""
Convert GeoPackage files into Apache Parquet.

Author: Big Data Analytics Project
"""

import sys
from pathlib import Path

import geopandas as gpd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from config.project_config import (
    PROCESSED_DATA_DIR,
    PARQUET_DATA_DIR
)

FILES = [
    ("roads.gpkg", "roads.parquet"),
    ("railways.gpkg", "railways.parquet"),
    ("airports.gpkg", "airports.parquet")
]


def convert(input_name, output_name):

    input_file = PROCESSED_DATA_DIR / input_name
    output_file = PARQUET_DATA_DIR / output_name

    print("=" * 60)
    print(f"Reading {input_name}")
    print("=" * 60)

    gdf = gpd.read_file(input_file)

    print(f"Features : {len(gdf):,}")

    print("Saving...")

    gdf.to_parquet(output_file)

    print(f"Created: {output_name}\n")


def main():

    PARQUET_DATA_DIR.mkdir(parents=True, exist_ok=True)

    for input_name, output_name in FILES:
        convert(input_name, output_name)

    print("=" * 60)
    print("ALL CONVERSIONS COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()
