from pyspark.sql import SparkSession, DataFrame

from src.models.customer_schema import customer_schema


def read_customer(spark: SparkSession, file_path: str) -> DataFrame:

    customer_df = (
        spark.read
        .option("header", True)
        .schema(customer_schema)
        .csv(file_path)
    )

    return customer_df