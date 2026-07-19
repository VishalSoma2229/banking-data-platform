from pyspark.sql import DataFrame


def write_gold(df: DataFrame, output_path: str):
    """
    Write Gold layer data to MinIO.
    """

    (
        df.write
        .mode("overwrite")
        .parquet(output_path)
    )