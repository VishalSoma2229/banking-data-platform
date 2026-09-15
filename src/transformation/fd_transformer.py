from pyspark.sql import DataFrame
from pyspark.sql.functions import col,trim,upper,initcap,current_timestamp

def transform_fd(df:DataFrame)->DataFrame:
    return (df.dropDuplicates(["fd_id"])
.withColumn("customer_id",trim(col("customer_id")))
.withColumn("fd_status",upper(trim(col("fd_status"))))
.withColumn("ingestion_timestamp",current_timestamp()))
