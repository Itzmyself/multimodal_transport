"""
Clean transportation datasets and normalize schemas.

Output:
    roads_clean.parquet
    railways_clean.parquet
    airports_clean.parquet
"""

import sys
from pathlib import Path

import geopandas as gpd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from config.project_config import PARQUET_DATA_DIR


def clean_dataset(input_file, output_file, subtype_column, transport_type):

    print("=" * 60)
    print(f"Cleaning {input_file}")
    print("=" * 60)

    gdf = gpd.read_parquet(PARQUET_DATA_DIR / input_file)

    columns = ["osm_id", "name", subtype_column, "geometry"]

    gdf = gdf[columns].copy()

    gdf.rename(
        columns={
            subtype_column: "transport_subtype"
        },
        inplace=True
    )

    gdf["transport_type"] = transport_type

    gdf = gdf[
        [
            "osm_id",
            "name",
            "transport_type",
            "transport_subtype",
            "geometry"
        ]
    ]

    output_path = PARQUET_DATA_DIR / output_file

    gdf.to_parquet(output_path)

    print(f"Rows : {len(gdf):,}")
    print(f"Saved : {output_path}\n")


def main():

    clean_dataset(
        "roads.parquet",
        "roads_clean.parquet",
        "highway",
        "road"
    )

    clean_dataset(
        "railways.parquet",
        "railways_clean.parquet",
        "railway",
        "railway"
    )

    clean_dataset(
        "airports.parquet",
        "airports_clean.parquet",
        "aerialway",
        "airport"
    )

    print("=" * 60)
    print("ALL DATASETS CLEANED")
    print("=" * 60)


if __name__ == "__main__":
    main()
