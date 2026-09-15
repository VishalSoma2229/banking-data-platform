from pyspark.sql import DataFrame
from pyspark.sql.functions import col,trim,upper,initcap,current_timestamp

def transform_account(df:DataFrame)->DataFrame:
    return (df.dropDuplicates(["account_id"])
.withColumn("account_type",upper(trim(col("account_type"))))
.withColumn("currency",upper(trim(col("currency"))))
.withColumn("account_status",upper(trim(col("account_status"))))
.withColumn("account_number",trim(col("account_number")))
.withColumn("ingestion_timestamp",current_timestamp()))
