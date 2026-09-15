from datetime import datetime

import sys

from airflow import DAG
from airflow.operators.python import PythonOperator


sys.path.insert(0, "/opt/airflow/project")

from src.pipelines.transaction_pipeline import (
    run_transaction_bronze,
    run_transaction_silver,
    run_transaction_gold,
)

with DAG(
    dag_id="transaction_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    default_args={"owner": "vishal", "retries": 1},
    tags=["banking", "transaction", "medallion"],
) as dag:

    bronze = PythonOperator(
        task_id="transaction_bronze",
        python_callable=run_transaction_bronze,
    )

    silver = PythonOperator(
        task_id="transaction_silver",
        python_callable=run_transaction_silver,
    )

    gold = PythonOperator(
        task_id="transaction_gold",
        python_callable=run_transaction_gold,
    )

    bronze >> silver >> gold
