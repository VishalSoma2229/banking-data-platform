from datetime import datetime
import sys


from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, "/opt/airflow/project")

from src.pipelines.branch_pipeline import (
    run_branch_bronze,
    run_branch_silver,
    run_branch_gold,
)

with DAG(
    dag_id="branch_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    default_args={"owner": "vishal", "retries": 1},
    tags=["banking", "branch", "medallion"],
) as dag:

    bronze = PythonOperator(
        task_id="branch_bronze",
        python_callable=run_branch_bronze,
    )

    silver = PythonOperator(
        task_id="branch_silver",
        python_callable=run_branch_silver,
    )

    gold = PythonOperator(
        task_id="branch_gold",
        python_callable=run_branch_gold,
    )

    bronze >> silver >> gold
