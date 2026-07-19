from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    trim,
    upper,
    initcap,
    current_timestamp,
    col
)


def transform_customer(df: DataFrame) -> DataFrame:

    df = df.dropDuplicates(["customer_id"])

    df = (
        df.withColumn(
            "first_name",
            initcap(trim(col("first_name")))
        )
        .withColumn(
            "last_name",
            initcap(trim(col("last_name")))
        )
    )

    text_columns = [
        "gender",
        "marital_status",
        "kyc_status",
        "risk_category",
        "customer_status",
        "country"
    ]

    for column in text_columns:
        df = df.withColumn(
            column,
            upper(trim(col(column)))
        )

    df = df.withColumn(
        "email",
        trim(col("email"))
    )

    df = df.withColumn(
        "phone",
        trim(col("phone"))
    )

    df = df.withColumn(
        "pan_number",
        upper(trim(col("pan_number")))
    )

    df = df.withColumn(
        "aadhaar_number",
        trim(col("aadhaar_number"))
    )

    df = df.withColumn(
        "ingestion_timestamp",
        current_timestamp()
    )

    return df