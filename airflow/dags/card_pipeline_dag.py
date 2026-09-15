from datetime import datetime
import sys


from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, "/opt/airflow/project")

from src.pipelines.card_pipeline import (
    run_card_bronze,
    run_card_silver,
    run_card_gold,
)

with DAG(
    dag_id="card_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    default_args={"owner": "vishal", "retries": 1},
    tags=["banking", "card", "medallion"],
) as dag:

    bronze = PythonOperator(
        task_id="card_bronze",
        python_callable=run_card_bronze,
    )

    silver = PythonOperator(
        task_id="card_silver",
        python_callable=run_card_silver,
    )

    gold = PythonOperator(
        task_id="card_gold",
        python_callable=run_card_gold,
    )

    bronze >> silver >> gold
