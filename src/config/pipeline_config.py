from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Source Data
CUSTOMER_SOURCE_PATH = str(
    PROJECT_ROOT / "datasets" / "source" / "customer" / "CUSTOMER_MASTER.csv"
)

# Bronze
CUSTOMER_BRONZE_PATH = "s3a://banking-lake/bronze/customer/"

# Silver
CUSTOMER_SILVER_PATH = "s3a://banking-lake/silver/customer/"

# Gold
CUSTOMER_GOLD_PATH = "s3a://banking-lake/gold/customer/"

# Rejected
CUSTOMER_REJECTED_PATH = "s3a://banking-lake/rejected/customer/"