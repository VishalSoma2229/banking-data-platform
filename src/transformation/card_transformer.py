from pyspark.sql import DataFrame
from pyspark.sql.functions import col,trim,upper,initcap,current_timestamp

def transform_card(df:DataFrame)->DataFrame:
    return (df.dropDuplicates(["card_id"])
.withColumn("account_id",trim(col("account_id")))
.withColumn("card_type",upper(trim(col("card_type"))))
.withColumn("network",upper(trim(col("network"))))
.withColumn("card_status",upper(trim(col("card_status"))))
.withColumn("ingestion_timestamp",current_timestamp()))
