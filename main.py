from src.common.spark_session import create_spark_session

from src.pipelines.customer_bronze_pipeline import run_customer_bronze
from src.pipelines.customer_silver_pipeline import run_customer_silver
from src.pipelines.customer_gold_pipeline import run_customer_gold


def main():

    spark = create_spark_session("Banking Data Platform")

    run_customer_bronze(spark)

    run_customer_silver(spark)

    run_customer_gold(spark)

    input("Press Enter to stop Spark...")

    spark.stop()


if __name__ == "__main__":
    main()