import pickle
import joblib
import pandas as pd
import networkx as nx

from geocode import geocode_place
from shortest_path import nearest_node
from generate_candidates import (
    estimate_travel_time,
    estimate_cost,
    estimate_carbon,
)


def load_graph():
    with open("data/graph/road_graph.pkl", "rb") as f:
        return pickle.load(f)


def load_model():
    return joblib.load("models/random_forest.pkl")


def generate_candidate_routes(distance):

    return [

        {
            "mode": "Road",
            "distance_km": distance,
            "travel_time_hr": estimate_travel_time(distance, 60),
            "travel_cost": estimate_cost(distance, 0.12),
            "transfers": 0,
            "delay_probability": 0.10,
            "crowd_level": 0.40,
            "weather_impact": 0.15,
            "safety_score": 0.95,
            "carbon_emission": estimate_carbon(distance, 0.18),
        },

        {
            "mode": "Road + Rail",
            "distance_km": distance * 1.08,
            "travel_time_hr": estimate_travel_time(distance * 1.08, 85),
            "travel_cost": estimate_cost(distance * 1.08, 0.08),
            "transfers": 1,
            "delay_probability": 0.15,
            "crowd_level": 0.55,
            "weather_impact": 0.12,
            "safety_score": 0.96,
            "carbon_emission": estimate_carbon(distance * 1.08, 0.07),
        },

        {
            "mode": "Road + Flight",
            "distance_km": distance * 0.75,
            "travel_time_hr": estimate_travel_time(distance * 0.75, 600),
            "travel_cost": estimate_cost(distance * 0.75, 0.45),
            "transfers": 1,
            "delay_probability": 0.22,
            "crowd_level": 0.65,
            "weather_impact": 0.25,
            "safety_score": 0.93,
            "carbon_emission": estimate_carbon(distance * 0.75, 0.30),
        },
    ]


print("=" * 60)
print("MULTIMODAL TRANSPORT RECOMMENDER")
print("=" * 60)

source = input("Source City: ")
destination = input("Destination City: ")

print("\nPreference")
print("1. Fastest")
print("2. Cheapest")
print("3. Eco Friendly")
print("4. Balanced")

choice = input("Choose option: ")

src = geocode_place(source)
dst = geocode_place(destination)

G = load_graph()

start = nearest_node(G, src["latitude"], src["longitude"])
end = nearest_node(G, dst["latitude"], dst["longitude"])

distance = nx.shortest_path_length(
    G,
    start,
    end,
    weight="distance"
) / 1000

routes = generate_candidate_routes(distance)

if choice == "1":
    routes = sorted(routes, key=lambda x: x["travel_time_hr"])

elif choice == "2":
    routes = sorted(routes, key=lambda x: x["travel_cost"])

elif choice == "3":
    routes = sorted(routes, key=lambda x: x["carbon_emission"])

model = load_model()

best_route = None
best_score = -1

for route in routes:

    X = pd.DataFrame([[
        route["distance_km"],
        route["travel_time_hr"],
        route["travel_cost"],
        route["transfers"],
        route["delay_probability"],
        route["crowd_level"],
        route["weather_impact"],
        route["safety_score"],
        route["carbon_emission"],
    ]], columns=[
        "distance_km",
        "travel_time_hr",
        "travel_cost",
        "transfers",
        "delay_probability",
        "crowd_level",
        "weather_impact",
        "safety_score",
        "carbon_emission",
    ])

    probability = model.predict_proba(X)[0][1]

    route["score"] = probability

    if probability > best_score:
        best_score = probability
        best_route = route

print("\n" + "=" * 60)
print("RECOMMENDED ROUTE")
print("=" * 60)

print(f"Mode            : {best_route['mode']}")
print(f"Distance        : {best_route['distance_km']:.2f} km")
print(f"Travel Time     : {best_route['travel_time_hr']:.2f} hr")
print(f"Travel Cost     : ${best_route['travel_cost']:.2f}")
print(f"Carbon Emission : {best_route['carbon_emission']:.2f} kg")
print(f"Transfers       : {best_route['transfers']}")
print(f"Recommendation  : {best_route['score']*100:.2f}%")
