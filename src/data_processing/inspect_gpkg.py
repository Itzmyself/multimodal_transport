import sys
from pathlib import Path

import fiona

# -------------------------------------------------------
# Add project root to Python path
# -------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from config.project_config import GPKG_FILE


def main():
    print("=" * 60)
    print("GeoPackage Inspection")
    print("=" * 60)

    print(f"\nGeoPackage File:\n{GPKG_FILE}")

    if not GPKG_FILE.exists():
        print("\nERROR: GeoPackage not found.")
        return

    print("\nAvailable Layers:\n")

    layers = fiona.listlayers(GPKG_FILE)

    for i, layer in enumerate(layers, start=1):
        print(f"{i}. {layer}")

    print("\nTotal Layers:", len(layers))


if __name__ == "__main__":
    main()
