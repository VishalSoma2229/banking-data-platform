from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    LongType,
    DoubleType,
    DecimalType,
    DateType,
    TimestampType,
    BooleanType
)

card_schema = StructType([
    StructField("card_id", StringType(), False),
    StructField("account_id", StringType(), False),
    StructField("card_type", StringType(), False),
    StructField("network", StringType(), False),
    StructField("issue_date", DateType(), False),
    StructField("expiry_date", DateType(), False),
    StructField("card_status", StringType(), False)
])
