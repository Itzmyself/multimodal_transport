import pickle
import networkx as nx
from geopy.distance import geodesic

from geocode import geocode_place


def nearest_node(graph, latitude, longitude):
    """
    Find the nearest node in the graph to the given coordinates.
    """

    nearest = None
    min_distance = float("inf")

    print("Searching nearest node...")

    for node in graph.nodes:

        dist = geodesic(
            (latitude, longitude),
            (node[1], node[0])
        ).meters

        if dist < min_distance:
            min_distance = dist
            nearest = node

    print(f"Nearest node found ({min_distance:.2f} m away)")

    return nearest


def main():

    print("=" * 60)
    print("SHORTEST PATH")
    print("=" * 60)

    source = input("Source City: ")
    destination = input("Destination City: ")

    src = geocode_place(source)
    dst = geocode_place(destination)

    print("\nLoading road graph...")

    with open("data/graph/road_graph.pkl", "rb") as f:
        G = pickle.load(f)

    start = nearest_node(
        G,
        src["latitude"],
        src["longitude"]
    )

    end = nearest_node(
        G,
        dst["latitude"],
        dst["longitude"]
    )

    print("\nRunning Dijkstra...")

    try:

        path = nx.shortest_path(
            G,
            start,
            end,
            weight="distance"
        )

        distance = nx.shortest_path_length(
            G,
            start,
            end,
            weight="distance"
        )

        print("\n========== RESULT ==========")
        print(f"Nodes in path : {len(path):,}")
        print(f"Distance      : {distance/1000:.2f} km")

    except nx.NetworkXNoPath:

        print("\nNo valid road path exists between these two locations.")
        print("Try two cities that are closer together.")


if __name__ == "__main__":
    main()
