from pyspark.sql import DataFrame
from pyspark.sql.functions import col,trim,upper,initcap,current_timestamp

def transform_transaction(df:DataFrame)->DataFrame:
    return (df.dropDuplicates(["transaction_id"])
.withColumn("transaction_type",upper(trim(col("transaction_type"))))
.withColumn("channel",upper(trim(col("channel"))))
.withColumn("currency",upper(trim(col("currency"))))
.withColumn("status",upper(trim(col("status"))))
.withColumn("fraud_flag",upper(trim(col("fraud_flag"))))
.withColumn("merchant",trim(col("merchant")))
.withColumn("ingestion_timestamp",current_timestamp()))
