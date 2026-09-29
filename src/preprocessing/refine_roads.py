"""
Refine the road dataset for routing.
"""

import sys
from pathlib import Path

from pyspark.sql.functions import col

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from src.spark.spark_session import create_spark_session
from src.preprocessing.filters import ROAD_CLASSES

BASE_PATH = "hdfs://localhost:9000/multimodal_transport_ca/parquet"


def main():

    spark = create_spark_session()

    print("=" * 70)
    print("Loading road dataset from HDFS")
    print("=" * 70)

    roads = spark.read.parquet(
        f"{BASE_PATH}/roads_normalized.parquet"
    )

    print(f"Original Records : {roads.count():,}")

    # Keep only routing road classes

    refined = roads.filter(
        col("highway").isin(ROAD_CLASSES)
    )

    print(f"Filtered Records : {refined.count():,}")

    print("\nRemaining Road Classes")

    refined.groupBy("highway") \
           .count() \
           .orderBy("highway") \
           .show(truncate=False)

    output_path = "data/parquet/roads_network.parquet"

    print("\nSaving refined dataset...")

    refined.write.mode("overwrite").parquet(output_path)

    print(f"\nSaved to: {output_path}")

    spark.stop()


if __name__ == "__main__":
    main()
