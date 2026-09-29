from pathlib import Path

import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Load training data
df = pd.read_csv("data/journeys/training_dataset.csv")

# Features
X = df[
    [
        "distance_km",
        "travel_time_hr",
        "travel_cost",
        "transfers",
        "delay_probability",
        "crowd_level",
        "weather_impact",
        "safety_score",
        "carbon_emission",
    ]
]

# Target
y = df["recommended"]

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
)

model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"\nAccuracy: {accuracy:.4f}")

# Save model
Path("models").mkdir(exist_ok=True)

joblib.dump(model, "models/random_forest.pkl")

print("\nModel saved to:")
print("models/random_forest.pkl")
