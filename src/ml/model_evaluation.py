from pathlib import Path
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATASET = PROJECT_ROOT / "data" / "journeys" / "training_dataset.csv"
MODEL = PROJECT_ROOT / "models" / "random_forest.pkl"

# Load dataset
df = pd.read_csv(DATASET)

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
        "carbon_emission"
    ]
]

y = df["recommended"]

# Same split used during training
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Load trained model
model = joblib.load(MODEL)

# Predictions
y_pred = model.predict(X_test)

print("=" * 60)
print("MODEL EVALUATION")
print("=" * 60)

print(f"Accuracy  : {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision : {precision_score(y_test, y_pred):.4f}")
print(f"Recall    : {recall_score(y_test, y_pred):.4f}")
print(f"F1 Score  : {f1_score(y_test, y_pred):.4f}")

print("\nConfusion Matrix")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))
