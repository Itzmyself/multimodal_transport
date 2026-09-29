import sys
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from config.project_config import PARQUET_DATA_DIR

FILES = [

    "roads_normalized.parquet",

    "railways_normalized.parquet",

    "airports_normalized.parquet"

]

for file in FILES:

    print("="*60)

    print(file)

    print("="*60)

    df = pd.read_parquet(
        PARQUET_DATA_DIR / file
    )

    print(df.head())

    print()

    print(df.columns.tolist())

    print()

    print(df["transport_type"].value_counts())

    print("\n")
