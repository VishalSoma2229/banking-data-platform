from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    current_date,
    datediff,
    floor,
    concat_ws
)


def transform_customer_gold(df: DataFrame) -> DataFrame:

    df = df.withColumn(
        "customer_name",
        concat_ws(" ", col("first_name"), col("last_name"))
    )

    df = df.withColumn(
        "customer_age",
        floor(
            datediff(
                current_date(),
                col("date_of_birth")
            ) / 365.25
        )
    )

    df = df.withColumn(
        "customer_tenure_days",
        datediff(
            current_date(),
            col("customer_since")
        )
    )

    return df