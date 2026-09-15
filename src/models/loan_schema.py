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

loan_schema = StructType([
    StructField("loan_id", StringType(), False),
    StructField("customer_id", StringType(), False),
    StructField("loan_type", StringType(), False),
    StructField("principal", DecimalType(9, 2), False),
    StructField("interest_rate", DecimalType(4, 2), False),
    StructField("tenure_months", LongType(), False),
    StructField("loan_status", StringType(), False)
])