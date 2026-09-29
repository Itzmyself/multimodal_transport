"""
Normalize transportation datasets.

Author:
Big Data Analytics Project
"""

import sys
from pathlib import Path

import geopandas as gpd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from config.project_config import PARQUET_DATA_DIR


FILES = [

    (
        "roads.parquet",
        "roads_normalized.parquet",
        "road"
    ),

    (
        "railways.parquet",
        "railways_normalized.parquet",
        "railway"
    ),

    (
        "airports.parquet",
        "airports_normalized.parquet",
        "airport"
    )

]


def normalize(input_file,
              output_file,
              transport_type):

    print("=" * 60)
    print(input_file)
    print("=" * 60)

    gdf = gpd.read_parquet(
        PARQUET_DATA_DIR / input_file
    )

    # -----------------------------
    # Keep only useful columns
    # -----------------------------

    columns = [
        "osm_id",
        "name",
        "highway",
        "other_tags",
        "geometry"
    ]

    keep = []

    for c in columns:

        if c in gdf.columns:
            keep.append(c)

    gdf = gdf[keep].copy()

    gdf["transport_type"] = transport_type

    # -----------------------------
    # Put columns in fixed order
    # -----------------------------

    final_columns = [
        "osm_id",
        "name",
        "transport_type",
        "highway",
        "other_tags",
        "geometry"
    ]

    final_columns = [
        c for c in final_columns
        if c in gdf.columns
    ]

    gdf = gdf[final_columns]

    output_path = PARQUET_DATA_DIR / output_file

    gdf.to_parquet(output_path)

    print(f"Rows : {len(gdf):,}")
    print("Done.\n")


def main():

    for f in FILES:

        normalize(*f)

    print("=" * 60)
    print("NORMALIZATION COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
