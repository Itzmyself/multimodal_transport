from pathlib import Path
import pandas as pd
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT = PROJECT_ROOT / "data" / "journeys" / "training_dataset.csv"

np.random.seed(42)

N = 5000

modes = ["Road", "Rail", "Flight"]

rows = []

for i in range(N):

    mode = np.random.choice(modes)

    if mode == "Road":
        distance = np.random.randint(10, 500)
        speed = np.random.uniform(40, 70)
        cost = distance * 0.15
        transfers = 0
        carbon = distance * 0.15

    elif mode == "Rail":
        distance = np.random.randint(20, 800)
        speed = np.random.uniform(60, 110)
        cost = distance * 0.08
        transfers = np.random.randint(1, 3)
        carbon = distance * 0.05

    else:
        distance = np.random.randint(100, 2500)
        speed = np.random.uniform(500, 800)
        cost = distance * 0.25
        transfers = np.random.randint(1, 3)
        carbon = distance * 0.45

    travel_time = distance / speed

    delay = np.random.uniform(0.05, 0.30)
    crowd = np.random.uniform(0.20, 0.90)
    weather = np.random.uniform(0.00, 0.40)
    safety = np.random.uniform(0.85, 0.99)

    score = (
        100
        - cost * 0.3
        - travel_time * 5
        - carbon * 0.2
        - delay * 20
    )

    recommendation = 1 if score >= 70 else 0

    rows.append({

        "transport_mode": mode,
        "distance_km": round(distance,2),
        "travel_time_hr": round(travel_time,2),
        "travel_cost": round(cost,2),
        "transfers": transfers,
        "delay_probability": round(delay,2),
        "crowd_level": round(crowd,2),
        "weather_impact": round(weather,2),
        "safety_score": round(safety,2),
        "carbon_emission": round(carbon,2),
        "recommended": recommendation

    })

df = pd.DataFrame(rows)

df.to_csv(OUTPUT,index=False)

print(df.head())

print()

print("Rows:",len(df))

print()

print("Saved:",OUTPUT)
