"""
Project Configuration File

Stores all important project paths in one place.
"""

from pathlib import Path

# ------------------------------------------------------------------
# Project Root
# ------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ------------------------------------------------------------------
# Data Directories
# ------------------------------------------------------------------

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"
INTERMEDIATE_DATA_DIR = DATA_DIR / "intermediate"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
PARQUET_DATA_DIR = DATA_DIR / "parquet"

# ------------------------------------------------------------------
# Raw Dataset
# ------------------------------------------------------------------

RAW_OSM_PBF = RAW_DATA_DIR / "central-america-260713.osm.pbf"

# ------------------------------------------------------------------
# Output Files
# ------------------------------------------------------------------

GPKG_FILE = PROCESSED_DATA_DIR / "central-america.gpkg"

# ------------------------------------------------------------------
# Other Project Directories
# ------------------------------------------------------------------

SRC_DIR = PROJECT_ROOT / "src"

SPARK_DIR = PROJECT_ROOT / "spark"

HADOOP_DIR = PROJECT_ROOT / "hadoop"

ML_DIR = PROJECT_ROOT / "ml"

MODELS_DIR = PROJECT_ROOT / "models"

REPORTS_DIR = PROJECT_ROOT / "reports"

LOGS_DIR = PROJECT_ROOT / "logs"

CONFIG_DIR = PROJECT_ROOT / "config"
