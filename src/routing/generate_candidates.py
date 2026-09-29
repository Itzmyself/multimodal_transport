import pickle
import networkx as nx

from geocode import geocode_place
from shortest_path import nearest_node


def estimate_travel_time(distance_km, speed):
    return distance_km / speed


def estimate_cost(distance_km, rate):
    return distance_km * rate


def estimate_carbon(distance_km, factor):
    return distance_km * factor


def main():

    print("=" * 60)
    print("CANDIDATE ROUTE GENERATOR")
    print("=" * 60)

    source = input("Source City: ")
    destination = input("Destination City: ")

    src = geocode_place(source)
    dst = geocode_place(destination)

    with open("data/graph/road_graph.pkl", "rb") as f:
        G = pickle.load(f)

    start = nearest_node(G, src["latitude"], src["longitude"])
    end = nearest_node(G, dst["latitude"], dst["longitude"])

    distance = nx.shortest_path_length(
        G,
        start,
        end,
        weight="distance"
    ) / 1000

    candidates = [

        {
            "mode": "Road",
            "distance": distance,
            "time": estimate_travel_time(distance, 60),
            "cost": estimate_cost(distance, 0.12),
            "carbon": estimate_carbon(distance, 0.18),
            "transfers": 0
        },

        {
            "mode": "Road + Rail",
            "distance": distance * 1.08,
            "time": estimate_travel_time(distance * 1.08, 85),
            "cost": estimate_cost(distance * 1.08, 0.08),
            "carbon": estimate_carbon(distance * 1.08, 0.07),
            "transfers": 1
        },

        {
            "mode": "Road + Flight",
            "distance": distance * 0.75,
            "time": estimate_travel_time(distance * 0.75, 600),
            "cost": estimate_cost(distance * 0.75, 0.45),
            "carbon": estimate_carbon(distance * 0.75, 0.30),
            "transfers": 1
        }

    ]

    print("\nCandidate Routes\n")

    for i, route in enumerate(candidates, start=1):

        print(f"Route {i}")
        print("-------------------------")
        print(f"Mode       : {route['mode']}")
        print(f"Distance   : {route['distance']:.2f} km")
        print(f"Time       : {route['time']:.2f} hr")
        print(f"Cost       : ${route['cost']:.2f}")
        print(f"Carbon     : {route['carbon']:.2f} kg")
        print(f"Transfers  : {route['transfers']}")
        print()


if __name__ == "__main__":
    main()
