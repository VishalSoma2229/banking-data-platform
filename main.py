from src.common.spark_session import create_spark_session

from src.pipelines.customer_bronze_pipeline import run_customer_bronze
from src.pipelines.customer_silver_pipeline import run_customer_silver
from src.pipelines.customer_gold_pipeline import run_customer_gold
from src.pipelines.account_pipeline import run_account_bronze
from src.pipelines.branch_pipeline import run_branch_bronze
from src.pipelines.card_pipeline import run_card_bronze
from src.pipelines.fd_pipeline import run_fd_bronze
from src.pipelines.loan_pipeline import run_loan_bronze
from src.pipelines.transaction_pipeline import run_transaction_bronze


def main():
    run_customer_bronze()
    run_customer_silver()
    run_customer_gold()
    run_account_bronze()
    run_branch_bronze()
    run_card_bronze()
    run_fd_bronze()
    run_loan_bronze()
    run_transaction_bronze()


if __name__ == '__main__':
    main()