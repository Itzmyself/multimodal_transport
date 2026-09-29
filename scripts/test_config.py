import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from config.project_config import *

print("=" * 60)
print("PROJECT CONFIGURATION")
print("=" * 60)

print(f"Project Root        : {PROJECT_ROOT}")
print(f"Raw Data Directory  : {RAW_DATA_DIR}")
print(f"Raw Dataset         : {RAW_OSM_PBF}")
print(f"Processed Directory : {PROCESSED_DATA_DIR}")
print(f"GeoPackage Output   : {GPKG_FILE}")
