from pyspark.sql import DataFrame
from pyspark.sql.functions import col,trim,upper,initcap,current_timestamp

def transform_loan(df:DataFrame)->DataFrame:
    return (df.dropDuplicates(["loan_id"])
.withColumn("customer_id",trim(col("customer_id")))
.withColumn("loan_type",upper(trim(col("loan_type"))))
.withColumn("loan_status",upper(trim(col("loan_status"))))
.withColumn("ingestion_timestamp",current_timestamp()))
