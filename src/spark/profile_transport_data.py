"""
Profile transportation datasets stored in HDFS using Spark.
"""

import sys
from pathlib import Path

from pyspark.sql.functions import col, isnull

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from src.spark.spark_session import create_spark_session


BASE_PATH = "hdfs://localhost:9000/multimodal_transport_ca/parquet"

FILES = [
    "roads_normalized.parquet",
    "railways_normalized.parquet",
    "airports_normalized.parquet"
]


def profile_dataset(spark, filename):

    print("\n" + "=" * 70)
    print(f"DATASET : {filename}")
    print("=" * 70)

    df = spark.read.parquet(f"{BASE_PATH}/{filename}")

    # -------------------------------------------------------
    # Total rows
    # -------------------------------------------------------

    total = df.count()

    print(f"\nTotal Records : {total:,}")

    # -------------------------------------------------------
    # Schema
    # -------------------------------------------------------

    print("\nSchema")

    df.printSchema()

    # -------------------------------------------------------
    # Missing names
    # -------------------------------------------------------

    missing_names = df.filter(
        col("name").isNull()
    ).count()

    print(f"\nMissing Names : {missing_names:,}")

    # -------------------------------------------------------
    # Transport type
    # -------------------------------------------------------

    print("\nTransport Type")

    df.groupBy("transport_type") \
      .count() \
      .show()

    # -------------------------------------------------------
    # Highway values
    # -------------------------------------------------------

    print("\nTop Highway Values")

    df.groupBy("highway") \
      .count() \
      .orderBy(col("count").desc()) \
      .show(15, truncate=False)

    # -------------------------------------------------------
    # Sample other_tags
    # -------------------------------------------------------

    print("\nSample other_tags")

    df.select("other_tags") \
      .where(col("other_tags").isNotNull()) \
      .show(10, truncate=False)


def main():

    spark = create_spark_session()

    for file in FILES:

        profile_dataset(spark, file)

    spark.stop()


if __name__ == "__main__":
    main()
