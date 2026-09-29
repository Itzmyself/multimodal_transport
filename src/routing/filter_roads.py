import geopandas as gpd

allowed_highways = [
    "motorway",
    "motorway_link",
    "trunk",
    "trunk_link",
    "primary",
    "primary_link",
    "secondary",
    "secondary_link",
    "tertiary",
    "tertiary_link",
    "residential",
    "unclassified",
    "living_street",
]

roads = gpd.read_file("data/regional/regional_roads.gpkg")

filtered = roads[roads["highway"].isin(allowed_highways)]

print("Original roads :", len(roads))
print("Filtered roads :", len(filtered))

filtered.to_file(
    "data/regional/regional_roads_filtered.gpkg",
    driver="GPKG"
)

print("\nSaved:")
print("data/regional/regional_roads_filtered.gpkg")
