"""
Read normalized transportation datasets from HDFS.
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from src.spark.spark_session import create_spark_session


BASE_PATH = "hdfs://localhost:9000/multimodal_transport_ca/parquet"

FILES = [
    "roads_normalized.parquet",
    "railways_normalized.parquet",
    "airports_normalized.parquet"
]


def main():

    spark = create_spark_session()

    for file in FILES:

        print("=" * 60)
        print(f"Reading {file}")
        print("=" * 60)

        path = f"{BASE_PATH}/{file}"

        df = spark.read.parquet(path)

        print("\nSchema:")
        df.printSchema()

        print(f"\nRows: {df.count():,}")

        print("\nSample Data:")
        df.show(5, truncate=False)

        print("\n")

    spark.stop()


if __name__ == "__main__":
    main()
