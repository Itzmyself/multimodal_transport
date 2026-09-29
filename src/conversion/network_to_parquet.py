"""
Convert refined transportation network GeoPackages to Parquet.
"""

import geopandas as gpd
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]

NETWORK_DIR = PROJECT_ROOT / "data" / "network"
PARQUET_DIR = PROJECT_ROOT / "data" / "parquet"


def convert(filename):

    input_file = NETWORK_DIR / filename
    output_file = PARQUET_DIR / filename.replace(".gpkg", ".parquet")

    print("=" * 70)
    print(f"Reading {filename}")
    print("=" * 70)

    gdf = gpd.read_file(input_file)

    print(f"Rows : {len(gdf):,}")

    gdf.to_parquet(output_file)

    print(f"Saved : {output_file}\n")


def main():

    convert("roads_network.gpkg")


if __name__ == "__main__":
    main()
