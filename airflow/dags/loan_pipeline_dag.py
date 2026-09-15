from datetime import datetime

import sys

from airflow import DAG
from airflow.operators.python import PythonOperator


sys.path.insert(0, "/opt/airflow/project")

from src.pipelines.loan_pipeline import (
    run_loan_bronze,
    run_loan_silver,
    run_loan_gold,
)

with DAG(
    dag_id="loan_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    default_args={"owner": "vishal", "retries": 1},
    tags=["banking", "loan", "medallion"],
) as dag:

    bronze = PythonOperator(
        task_id="loan_bronze",
        python_callable=run_loan_bronze,
    )

    silver = PythonOperator(
        task_id="loan_silver",
        python_callable=run_loan_silver,
    )

    gold = PythonOperator(
        task_id="loan_gold",
        python_callable=run_loan_gold,
    )

    bronze >> silver >> gold
