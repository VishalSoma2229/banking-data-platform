from pyspark.sql import DataFrame


def write_rejected(df: DataFrame, output_path: str):
    """
    Write rejected records to MinIO.
    """

    (
        df.write
        .mode("overwrite")
        .parquet(output_path)
    )