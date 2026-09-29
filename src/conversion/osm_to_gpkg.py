"""
Convert filtered OSM PBF files into GeoPackage files.

Input:
    roads.osm.pbf
    railways.osm.pbf
    airports.osm.pbf

Output:
    roads.gpkg
    railways.gpkg
    airports.gpkg
"""

import subprocess
from pathlib import Path
import sys

# ----------------------------------------------------
# Project root
# ----------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from config.project_config import PROCESSED_DATA_DIR

INTERMEDIATE_DIR = PROJECT_ROOT / "data" / "intermediate" / "osm"

FILES = [
    ("roads.osm.pbf", "roads.gpkg"),
    ("railways.osm.pbf", "railways.gpkg"),
    ("airports.osm.pbf", "airports.gpkg"),
]


def convert(input_file, output_file):

    input_path = INTERMEDIATE_DIR / input_file
    output_path = PROCESSED_DATA_DIR / output_file

    print("=" * 60)
    print(f"Converting {input_file}")
    print("=" * 60)

    command = [
        "ogr2ogr",
        "-f",
        "GPKG",
        str(output_path),
        str(input_path),
    ]

    result = subprocess.run(command)

    if result.returncode == 0:
        print(f"✓ Created {output_file}\n")
    else:
        print(f"✗ Failed to convert {input_file}\n")


def main():

    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    for input_file, output_file in FILES:
        convert(input_file, output_file)

    print("=" * 60)
    print("Conversion Completed")
    print("=" * 60)


if __name__ == "__main__":
    main()
