"""
Generate candidate transportation journeys.

Version 1:
Creates transportation combinations that will later
receive computed journey features.
"""

from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_DIR = PROJECT_ROOT / "data" / "journeys"

OUTPUT_FILE = OUTPUT_DIR / "candidate_journeys.csv"


def generate_candidates():

    journeys = [

        {
            "journey_id": 1,
            "transport_mode": "Road",
            "route": "Road"
        },

        {
            "journey_id": 2,
            "transport_mode": "Rail",
            "route": "Road -> Railway -> Road"
        },

        {
            "journey_id": 3,
            "transport_mode": "Flight",
            "route": "Road -> Flight -> Road"
        }

    ]

    df = pd.DataFrame(journeys)

    df.to_csv(OUTPUT_FILE, index=False)

    print("=" * 60)
    print("Candidate Journeys Generated")
    print("=" * 60)
    print(df)

    print()
    print("Saved:")
    print(OUTPUT_FILE)


if __name__ == "__main__":
    generate_candidates()
