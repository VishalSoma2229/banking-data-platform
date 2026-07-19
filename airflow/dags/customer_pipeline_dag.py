from datetime import datetime
import sys

from airflow import DAG
from airflow.operators.python import PythonOperator

# Add project root to Python path
sys.path.append("/opt/airflow/project")

from src.pipelines.customer_bronze_pipeline import run_customer_bronze
from src.pipelines.customer_silver_pipeline import run_customer_silver
from src.pipelines.customer_gold_pipeline import run_customer_gold


default_args = {
    "owner": "vishal",
    "depends_on_past": False,
    "retries": 1,
}


with DAG(
    dag_id="customer_data_pipeline",
    default_args=default_args,
    description="Customer Bronze → Silver → Gold Pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,          # Trigger manually
    catchup=False,
    tags=["banking", "customer", "pyspark"],
) as dag:

    bronze_task = PythonOperator(
        task_id="customer_bronze",
        python_callable=run_customer_bronze,
    )

    silver_task = PythonOperator(
        task_id="customer_silver",
        python_callable=run_customer_silver,
    )

    gold_task = PythonOperator(
        task_id="customer_gold",
        python_callable=run_customer_gold,
    )

    bronze_task >> silver_task >> gold_task