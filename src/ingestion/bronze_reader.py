from pyspark.sql import SparkSession
from pyspark.sql import DataFrame


def read_bronze(spark: SparkSession, input_path: str) -> DataFrame:
    """
    Read Bronze layer data from MinIO.
    """

    df = (
        spark.read
        .parquet(input_path)
    )

    return df