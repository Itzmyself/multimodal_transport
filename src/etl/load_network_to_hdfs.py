"""
Upload refined transportation network datasets to HDFS.
"""

import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

LOCAL_NETWORK = PROJECT_ROOT / "data" / "network"
HDFS_TARGET = "/multimodal_transport_ca/network"


def run(cmd):
    print(f"\n>>> {' '.join(cmd)}")
    subprocess.run(cmd, check=True)


def upload_dataset(filename):

    file_path = LOCAL_NETWORK / filename

    print(f"\nUploading {filename}")

    run([
        "hdfs",
        "dfs",
        "-put",
        "-f",
        str(file_path),
        HDFS_TARGET
    ])


def main():

    print("=" * 60)
    print("Creating HDFS Network Folder")
    print("=" * 60)

    run([
        "hdfs",
        "dfs",
        "-mkdir",
        "-p",
        HDFS_TARGET
    ])

    upload_dataset("roads_network.gpkg")

    print("\nUpload Complete")


if __name__ == "__main__":
    main()
