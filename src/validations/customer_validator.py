from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    current_date,
    lit,
    when,
    length
)


def validate_customer(df: DataFrame):

    validation_df = (

        df.withColumn(

            "rejection_reason",

            when(
                col("customer_id").isNull(),
                "Customer ID is NULL"
            )

            .when(
                col("first_name").isNull(),
                "First Name is NULL"
            )

            .when(
                col("last_name").isNull(),
                "Last Name is NULL"
            )

            .when(
                col("pan_number").isNull(),
                "PAN Number is NULL"
            )

            .when(
                col("aadhaar_number").isNull(),
                "Aadhaar Number is NULL"
            )

            .when(
                col("date_of_birth") > current_date(),
                "Future Date of Birth"
            )

            .when(
                ~col("email").rlike(
                    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
                ),
                "Invalid Email"
            )

            .when(
                length(col("phone")) != 10,
                "Invalid Phone Number"
            )

            .when(
                length(col("aadhaar_number")) != 12,
                "Invalid Aadhaar Number"
            )

            .when(
                ~col("pan_number").rlike(
                    r"^[A-Z]{5}[0-9]{4}[A-Z]$"
                ),
                "Invalid PAN Number"
            )

            .otherwise(lit(None))

        )

    )

    valid_df = (
        validation_df
        .filter(col("rejection_reason").isNull())
        .drop("rejection_reason")
    )

    invalid_df = (
        validation_df
        .filter(col("rejection_reason").isNotNull())
    )

    return valid_df, invalid_df