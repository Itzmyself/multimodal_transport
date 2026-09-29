from pathlib import Path

import geopandas as gpd
from shapely.geometry import LineString

from geocode import geocode_place


def create_corridor(src_lat, src_lon, dst_lat, dst_lon, buffer_distance=0.2):
    """
    Creates a corridor around the straight line joining
    source and destination.

    0.2 degrees ≈ 20–22 km.
    """

    line = LineString([
        (src_lon, src_lat),
        (dst_lon, dst_lat)
    ])

    return line.buffer(buffer_distance)


def extract_layer(gpkg_path, layer_name, corridor):

    gdf = gpd.read_file(gpkg_path, layer=layer_name)

    return gdf[gdf.geometry.intersects(corridor)]


def main():

    print("=" * 60)
    print("REGIONAL NETWORK EXTRACTION")
    print("=" * 60)

    source = input("Source City: ")
    destination = input("Destination City: ")

    src = geocode_place(source)
    dst = geocode_place(destination)

    if src is None or dst is None:
        print("Unable to geocode the locations.")
        return

    corridor = create_corridor(
        src["latitude"],
        src["longitude"],
        dst["latitude"],
        dst["longitude"],
        buffer_distance=0.2
    )

    print("\nExtracting Roads...")

    roads = extract_layer(
        "data/processed/roads.gpkg",
        "lines",
        corridor
    )

    print("Extracting Railways...")

    railways = extract_layer(
        "data/processed/railways.gpkg",
        "lines",
        corridor
    )

    print("Extracting Airports...")

    airports = extract_layer(
        "data/processed/airports.gpkg",
        "lines",
        corridor
    )

    output = Path("data/regional")
    output.mkdir(exist_ok=True)

    roads.to_file(
        output / "regional_roads.gpkg",
        driver="GPKG"
    )

    railways.to_file(
        output / "regional_railways.gpkg",
        driver="GPKG"
    )

    airports.to_file(
        output / "regional_airports.gpkg",
        driver="GPKG"
    )

    print("\nExtraction Complete")
    print("-------------------------")

    print(f"Roads     : {len(roads):,}")
    print(f"Railways  : {len(railways):,}")
    print(f"Airports  : {len(airports):,}")

    print("\nSaved to data/regional/")


if __name__ == "__main__":
    main()
