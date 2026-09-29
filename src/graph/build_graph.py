from pathlib import Path
import geopandas as gpd
import networkx as nx
import pickle

PROJECT_ROOT = Path(__file__).resolve().parents[2]

NETWORK_DIR = PROJECT_ROOT / "data" / "network"
GRAPH_DIR = PROJECT_ROOT / "data" / "graph"


def build_graph(input_file, output_file, graph_name):

    print("=" * 70)
    print(f"Building {graph_name}")
    print("=" * 70)

    gdf = gpd.read_file(input_file)

    print(f"Features : {len(gdf):,}")

    G = nx.Graph()

    for _, row in gdf.iterrows():

        geom = row.geometry

        if geom is None:
            continue

        if geom.geom_type != "LineString":
            continue

        coords = list(geom.coords)

        for i in range(len(coords) - 1):

            start = coords[i]
            end = coords[i + 1]

            distance = (
                (start[0] - end[0]) ** 2 +
                (start[1] - end[1]) ** 2
            ) ** 0.5

            G.add_edge(
                start,
                end,
                weight=distance
            )

    print(f"Nodes : {G.number_of_nodes():,}")
    print(f"Edges : {G.number_of_edges():,}")

    with open(output_file, "wb") as f:
        pickle.dump(G, f)

    print(f"Saved : {output_file}\n")


def main():

    build_graph(
        NETWORK_DIR / "roads_network.gpkg",
        GRAPH_DIR / "road_graph.pkl",
        "Road Graph"
    )

    build_graph(
        NETWORK_DIR / "railways_network.gpkg",
        GRAPH_DIR / "railway_graph.pkl",
        "Railway Graph"
    )


if __name__ == "__main__":
    main()
