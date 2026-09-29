import sys
from pathlib import Path

import geopandas as gpd
import fiona

# -----------------------------------------------------
# Add project root to Python path
# -----------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from config.project_config import GPKG_FILE

print("=" * 60)
print("TRANSPORT LAYER INSPECTION")
print("=" * 60)

print(f"\nReading GeoPackage:\n{GPKG_FILE}")

layers = fiona.listlayers(GPKG_FILE)

print("\nAvailable Layers:")

for layer in layers:
    print(f" - {layer}")

print("\nReading 'lines' layer...")

lines = gpd.read_file(GPKG_FILE, layer="lines")

print("\nNumber of features:", len(lines))

print("\nColumns:")

for column in lines.columns:
    print(column)
