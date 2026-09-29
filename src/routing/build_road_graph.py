from pathlib import Path
import pickle

import geopandas as gpd
import networkx as nx
from geopy.distance import geodesic
from shapely.geometry import LineString, MultiLineString


def add_linestring(graph, line):
    """
    Convert a LineString into graph edges.
    """
    coords = list(line.coords)

    for i in range(len(coords) - 1):

        p1 = coords[i]
        p2 = coords[i + 1]

        distance = geodesic(
            (p1[1], p1[0]),
            (p2[1], p2[0])
        ).meters

        graph.add_edge(
            p1,
            p2,
            distance=distance,
            mode="road"
        )


def main():

    print("=" * 60)
    print("BUILDING ROAD GRAPH")
    print("=" * 60)

    roads = gpd.read_file(
        "data/regional/regional_roads_filtered.gpkg"
    )

    print(f"Road features: {len(roads):,}")

    G = nx.Graph()

    processed = 0

    for _, row in roads.iterrows():

        geom = row.geometry

        if geom is None:
            continue

        if isinstance(geom, LineString):
            add_linestring(G, geom)

        elif isinstance(geom, MultiLineString):
            for line in geom.geoms:
                add_linestring(G, line)

        processed += 1

        if processed % 5000 == 0:
            print(f"Processed {processed:,} roads...")

    print("\nOriginal Graph")
    print("-------------------------")
    print(f"Nodes : {G.number_of_nodes():,}")
    print(f"Edges : {G.number_of_edges():,}")

    # Keep only the largest connected component
    largest_component = max(nx.connected_components(G), key=len)
    G = G.subgraph(largest_component).copy()

    print("\nLargest Connected Component")
    print("-------------------------")
    print(f"Nodes : {G.number_of_nodes():,}")
    print(f"Edges : {G.number_of_edges():,}")

    Path("data/graph").mkdir(parents=True, exist_ok=True)

    with open("data/graph/road_graph.pkl", "wb") as f:
        pickle.dump(G, f)

    print("\nGraph saved:")
    print("data/graph/road_graph.pkl")


if __name__ == "__main__":
    main()
