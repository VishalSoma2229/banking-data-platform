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

account_schema = StructType([
    StructField("account_id", StringType(), False),
    StructField("customer_id", StringType(), False),
    StructField("branch_id", StringType(), False),
    StructField("account_number", StringType(), False),
    StructField("account_type", StringType(), False),
    StructField("currency", StringType(), False),
    StructField("balance", DecimalType(9, 2), False),
    StructField("account_status", StringType(), False),
    StructField("opened_date", DateType(), False)
])