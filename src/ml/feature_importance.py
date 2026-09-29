from pathlib import Path
import joblib
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL = PROJECT_ROOT / "models" / "random_forest.pkl"

model = joblib.load(MODEL)

features = [
    "distance_km",
    "travel_time_hr",
    "travel_cost",
    "transfers",
    "delay_probability",
    "crowd_level",
    "weather_impact",
    "safety_score",
    "carbon_emission"
]

importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("=" * 60)
print("FEATURE IMPORTANCE")
print("=" * 60)

print(importance.to_string(index=False))
