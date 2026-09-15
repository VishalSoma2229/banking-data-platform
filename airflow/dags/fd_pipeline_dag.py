from datetime import datetime
import sys

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, "/opt/airflow/project")

from src.pipelines.fd_pipeline import (
    run_fd_bronze,
    run_fd_silver,
    run_fd_gold,
)

with DAG(
    dag_id="fd_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    default_args={"owner": "vishal", "retries": 1},
    tags=["banking", "fd", "medallion"],
) as dag:

    bronze = PythonOperator(
        task_id="fd_bronze",
        python_callable=run_fd_bronze,
    )

    silver = PythonOperator(
        task_id="fd_silver",
        python_callable=run_fd_silver,
    )

    gold = PythonOperator(
        task_id="fd_gold",
        python_callable=run_fd_gold,
    )

    bronze >> silver >> gold
