"""
Journey Feature Engineering
Version 1
"""

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = PROJECT_ROOT / "data" / "journeys" / "candidate_journeys.csv"

OUTPUT_FILE = PROJECT_ROOT / "data" / "journeys" / "journey_features.csv"


def build_features():

    df = pd.read_csv(INPUT_FILE)

    feature_rows = []

    for _, row in df.iterrows():

        route = row["route"]

        if route == "Road":

            feature_rows.append({

                "journey_id": row["journey_id"],
                "transport_mode": row["transport_mode"],

                "distance_km": 120,
                "travel_time_hr": 2.5,
                "travel_cost": 18,
                "transfers": 0,
                "delay_probability": 0.10,
                "crowd_level": 0.40,
                "weather_impact": 0.20,
                "safety_score": 0.90,
                "carbon_emission": 18

            })

        elif route == "Road -> Railway -> Road":

            feature_rows.append({

                "journey_id": row["journey_id"],
                "transport_mode": row["transport_mode"],

                "distance_km": 120,
                "travel_time_hr": 2.2,
                "travel_cost": 12,
                "transfers": 2,
                "delay_probability": 0.18,
                "crowd_level": 0.70,
                "weather_impact": 0.15,
                "safety_score": 0.95,
                "carbon_emission": 6

            })

        elif route == "Road -> Flight -> Road":

            feature_rows.append({

                "journey_id": row["journey_id"],
                "transport_mode": row["transport_mode"],

                "distance_km": 120,
                "travel_time_hr": 1.3,
                "travel_cost": 70,
                "transfers": 2,
                "delay_probability": 0.25,
                "crowd_level": 0.60,
                "weather_impact": 0.30,
                "safety_score": 0.98,
                "carbon_emission": 60

            })

    features = pd.DataFrame(feature_rows)

    features.to_csv(OUTPUT_FILE, index=False)

    print("=" * 60)
    print("Journey Features")
    print("=" * 60)

    print(features)

    print()

    print("Saved:")

    print(OUTPUT_FILE)


if __name__ == "__main__":
    build_features()
