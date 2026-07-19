from pyspark.sql import DataFrame


def write_bronze(customer_df: DataFrame, output_path: str) -> None:
    """
    Writes the DataFrame to the Bronze layer in Parquet format.
    """

    (
        customer_df.write
        .mode("overwrite")
        .parquet(output_path)
    )