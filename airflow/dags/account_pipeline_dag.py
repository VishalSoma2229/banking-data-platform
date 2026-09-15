from datetime import datetime
import sys

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, "/opt/airflow/project")

from src.pipelines.account_pipeline import (
    run_account_bronze,
    run_account_silver,
    run_account_gold,
)

with DAG(
    dag_id="account_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    default_args={"owner": "vishal", "retries": 1},
    tags=["banking", "account", "medallion"],
) as dag:

    bronze = PythonOperator(
        task_id="account_bronze",
        python_callable=run_account_bronze,
    )

    silver = PythonOperator(
        task_id="account_silver",
        python_callable=run_account_silver,
    )

    gold = PythonOperator(
        task_id="account_gold",
        python_callable=run_account_gold,
    )

    bronze >> silver >> gold
