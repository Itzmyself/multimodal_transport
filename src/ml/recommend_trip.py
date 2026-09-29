from pathlib import Path
import pandas as pd
import joblib

# -------------------------------------------------
# Project Paths
# -------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = PROJECT_ROOT / "models" / "random_forest.pkl"

# -------------------------------------------------
# Load Trained Model
# -------------------------------------------------

model = joblib.load(MODEL_PATH)

# -------------------------------------------------
# User Input
# -------------------------------------------------

print("=" * 60)
print("MULTIMODAL TRANSPORT RECOMMENDATION SYSTEM")
print("=" * 60)

distance = float(input("Distance (km): "))
travel_time = float(input("Travel Time (hr): "))
travel_cost = float(input("Travel Cost: "))
transfers = int(input("Number of Transfers: "))
delay_probability = float(input("Delay Probability (0-1): "))
crowd_level = float(input("Crowd Level (0-1): "))
weather_impact = float(input("Weather Impact (0-1): "))
safety_score = float(input("Safety Score (0-1): "))
carbon_emission = float(input("Carbon Emission: "))

# -------------------------------------------------
# Create DataFrame
# -------------------------------------------------

sample_trip = pd.DataFrame([{
    "distance_km": distance,
    "travel_time_hr": travel_time,
    "travel_cost": travel_cost,
    "transfers": transfers,
    "delay_probability": delay_probability,
    "crowd_level": crowd_level,
    "weather_impact": weather_impact,
    "safety_score": safety_score,
    "carbon_emission": carbon_emission
}])

# -------------------------------------------------
# Prediction
# -------------------------------------------------

prediction = model.predict(sample_trip)[0]
probability = model.predict_proba(sample_trip)[0]

# -------------------------------------------------
# Output
# -------------------------------------------------

print("\n" + "=" * 60)
print("TRANSPORT RECOMMENDATION")
print("=" * 60)

print(sample_trip)

print()

if prediction == 1:
    print("Recommendation : Recommended")
else:
    print("Recommendation : Not Recommended")

print(f"Confidence      : {probability[1] * 100:.2f}%")
