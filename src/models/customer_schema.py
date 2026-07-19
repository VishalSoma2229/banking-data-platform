from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DateType,
    DecimalType
)

customer_schema = StructType([

    StructField("customer_id", StringType(), False),

    StructField("first_name", StringType(), False),

    StructField("last_name", StringType(), False),

    StructField("gender", StringType(), True),

    StructField("date_of_birth", DateType(), False),

    StructField("email", StringType(), True),

    StructField("phone", StringType(), True),

    StructField("pan_number", StringType(), False),

    StructField("aadhaar_number", StringType(), False),

    StructField("occupation", StringType(), True),

    StructField("annual_income", DecimalType(12, 2), True),

    StructField("marital_status", StringType(), True),

    StructField("customer_since", DateType(), False),

    StructField("kyc_status", StringType(), False),

    StructField("risk_category", StringType(), False),

    StructField("branch_id", StringType(), False),

    StructField("city", StringType(), True),

    StructField("state", StringType(), True),

    StructField("country", StringType(), False),

    StructField("customer_status", StringType(), False)

])