from datetime import date

from src.transformation.customer_gold_transformer import (
    transform_customer_gold,
)


def test_gold_creates_customer_name(spark):

    data = [
        (
            "Vishal",
            "Soma",
            date(2000, 1, 1),
            date(2022, 1, 1)
        )
    ]

    columns = [
        "first_name",
        "last_name",
        "date_of_birth",
        "customer_since"
    ]

    df = spark.createDataFrame(data, columns)

    row = transform_customer_gold(df).first()

    assert row.customer_name == "Vishal Soma"


def test_gold_creates_customer_age(spark):

    data = [
        (
            "Vishal",
            "Soma",
            date(2000, 1, 1),
            date(2022, 1, 1)
        )
    ]

    columns = [
        "first_name",
        "last_name",
        "date_of_birth",
        "customer_since"
    ]

    df = spark.createDataFrame(data, columns)

    row = transform_customer_gold(df).first()

    assert row.customer_age >= 20
    assert row.customer_tenure_days > 0