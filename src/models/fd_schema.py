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

fd_schema = StructType([
    StructField("fd_id", StringType(), False),
    StructField("customer_id", StringType(), False),
    StructField("deposit_amount", DecimalType(9, 2), False),
    StructField("interest_rate", DecimalType(3, 2), False),
    StructField("maturity_date", DateType(), False),
    StructField("fd_status", StringType(), False)
])