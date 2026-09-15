from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parents[2]

CUSTOMER_SOURCE_PATH = str(PROJECT_ROOT / "datasets/source/customer/CUSTOMER_MASTER.csv")
ACCOUNT_SOURCE_PATH = str(PROJECT_ROOT / "datasets/source/account/ACCOUNT_MASTER.csv")
BRANCH_SOURCE_PATH = str(PROJECT_ROOT / "datasets/source/branch/BRANCH_MASTER.csv")
CARD_SOURCE_PATH = str(PROJECT_ROOT / "datasets/source/card/CARD_MASTER.csv")
FD_SOURCE_PATH = str(PROJECT_ROOT / "datasets/source/fd/FD_MASTER.csv")
LOAN_SOURCE_PATH = str(PROJECT_ROOT / "datasets/source/loan/LOAN_MASTER.csv")
TRANSACTION_SOURCE_PATH = str(PROJECT_ROOT / "datasets/source/transaction/TRANSACTION_MASTER.csv")

CUSTOMER_BRONZE_PATH = "s3a://banking-lake/bronze/customer/"
CUSTOMER_SILVER_PATH = "s3a://banking-lake/silver/customer/"
CUSTOMER_GOLD_PATH = "s3a://banking-lake/gold/customer/"
CUSTOMER_REJECTED_PATH = "s3a://banking-lake/rejected/customer/"

ACCOUNT_BRONZE_PATH="s3a://banking-lake/bronze/account/"
ACCOUNT_SILVER_PATH="s3a://banking-lake/silver/account/"
ACCOUNT_GOLD_PATH="s3a://banking-lake/gold/account/"
ACCOUNT_REJECTED_PATH="s3a://banking-lake/rejected/account/"

BRANCH_BRONZE_PATH="s3a://banking-lake/bronze/branch/"
BRANCH_SILVER_PATH="s3a://banking-lake/silver/branch/"
BRANCH_GOLD_PATH="s3a://banking-lake/gold/branch/"
BRANCH_REJECTED_PATH="s3a://banking-lake/rejected/branch/"

CARD_BRONZE_PATH="s3a://banking-lake/bronze/card/"
CARD_SILVER_PATH="s3a://banking-lake/silver/card/"
CARD_GOLD_PATH="s3a://banking-lake/gold/card/"
CARD_REJECTED_PATH="s3a://banking-lake/rejected/card/"

FD_BRONZE_PATH="s3a://banking-lake/bronze/fd/"
FD_SILVER_PATH="s3a://banking-lake/silver/fd/"
FD_GOLD_PATH="s3a://banking-lake/gold/fd/"
FD_REJECTED_PATH="s3a://banking-lake/rejected/fd/"

LOAN_BRONZE_PATH="s3a://banking-lake/bronze/loan/"
LOAN_SILVER_PATH="s3a://banking-lake/silver/loan/"
LOAN_GOLD_PATH="s3a://banking-lake/gold/loan/"
LOAN_REJECTED_PATH="s3a://banking-lake/rejected/loan/"

TRANSACTION_BRONZE_PATH="s3a://banking-lake/bronze/transaction/"
TRANSACTION_SILVER_PATH="s3a://banking-lake/silver/transaction/"
TRANSACTION_GOLD_PATH="s3a://banking-lake/gold/transaction/"
TRANSACTION_REJECTED_PATH="s3a://banking-lake/rejected/transaction/"
