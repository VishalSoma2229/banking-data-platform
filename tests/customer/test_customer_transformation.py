from src.transformation.customer_transformer import transform_customer


COLUMNS = [
    "customer_id",
    "first_name",
    "last_name",
    "gender",
    "marital_status",
    "kyc_status",
    "risk_category",
    "customer_status",
    "country",
    "email",
    "phone",
    "pan_number",
    "aadhaar_number"
]


def test_transform_customer_removes_duplicates(spark):

    data = [
        (
            1,
            " Vishal ",
            " Soma ",
            "male",
            "single",
            "verified",
            "low",
            "active",
            "india",
            "vishal.soma@example.com",
            "9876543210",
            "abcde1234f",
            "123456789012"
        ),
        (
            1,
            " Vishal ",
            " Soma ",
            "male",
            "single",
            "verified",
            "low",
            "active",
            "india",
            "vishal.soma@example.com",
            "9876543210",
            "abcde1234f",
            "123456789012"
        )
    ]

    df = spark.createDataFrame(data, COLUMNS)

    result = transform_customer(df)

    assert result.count() == 1


def test_transform_customer_trims_names(spark):

    data = [
        (
            1,
            "  Vishal  ",
            "  Soma  ",
            "male",
            "single",
            "verified",
            "low",
            "active",
            "india",
            "  vishal.soma@example.com  ",
            "9876543210",
            "abcde1234f",
            "123456789012"
        )
    ]

    df = spark.createDataFrame(data, COLUMNS)

    row = transform_customer(df).first()

    assert row.first_name == "Vishal"
    assert row.last_name == "Soma"


def test_transform_customer_uppercases_columns(spark):

    data = [
        (
            1,
            "Vishal",
            "Soma",
            "male",
            "single",
            "verified",
            "low",
            "active",
            "india",
            "vishal.soma@example.com",
            "9876543210",
            "abcde1234f",
            "123456789012"
        )
    ]

    df = spark.createDataFrame(data, COLUMNS)

    row = transform_customer(df).first()

    assert row.gender == "MALE"
    assert row.country == "INDIA"
    assert row.customer_status == "ACTIVE"
    assert row.pan_number == "ABCDE1234F"