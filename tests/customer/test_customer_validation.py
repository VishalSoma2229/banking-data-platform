from datetime import date

from src.validations.customer_validator import validate_customer


COLUMNS = [
    "customer_id",
    "first_name",
    "last_name",
    "pan_number",
    "aadhaar_number",
    "date_of_birth",
    "email",
    "phone"
]


def test_validate_customer_valid_record(spark):

    data = [
        (
            1,
            "Vishal",
            "Soma",
            "ABCDE1234F",
            "123456789012",
            date(2000, 1, 1),
            "vishal.soma@example.com",
            "9876543210"
        )
    ]

    df = spark.createDataFrame(data, COLUMNS)

    valid_df, invalid_df = validate_customer(df)

    assert valid_df.count() == 1
    assert invalid_df.count() == 0


def test_validate_customer_invalid_email(spark):

    data = [
        (
            1,
            "Vishal",
            "Soma",
            "ABCDE1234F",
            "123456789012",
            date(2000, 1, 1),
            "invalid_email",
            "9876543210"
        )
    ]

    df = spark.createDataFrame(data, COLUMNS)

    _, invalid_df = validate_customer(df)

    row = invalid_df.first()

    assert row.rejection_reason == "Invalid Email"


def test_validate_customer_invalid_pan(spark):

    data = [
        (
            1,
            "Vishal",
            "Soma",
            "12345",
            "123456789012",
            date(2000, 1, 1),
            "vishal.soma@example.com",
            "9876543210"
        )
    ]

    df = spark.createDataFrame(data, COLUMNS)

    _, invalid_df = validate_customer(df)

    row = invalid_df.first()

    assert row.rejection_reason == "Invalid PAN Number"