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

branch_schema = StructType([
    StructField("branch_id", StringType(), False),
    StructField("branch_name", StringType(), False),
    StructField("ifsc_code", StringType(), False),
    StructField("city", StringType(), False),
    StructField("state", StringType(), False),
    StructField("region", StringType(), False),
    StructField("opening_date", DateType(), False)
])