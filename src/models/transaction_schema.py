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

transaction_schema = StructType([
    StructField("transaction_id", StringType(), False),
    StructField("account_id", StringType(), False),
    StructField("transaction_timestamp", TimestampType(), False),
    StructField("transaction_type", StringType(), False),
    StructField("channel", StringType(), False),
    StructField("merchant", StringType(), False),
    StructField("amount", DecimalType(8, 2), False),
    StructField("currency", StringType(), False),
    StructField("status", StringType(), False),
    StructField("fraud_flag", StringType(), False)
])