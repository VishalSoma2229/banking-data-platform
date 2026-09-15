from pyspark.sql import DataFrame
from pyspark.sql.functions import col,to_date,hour,when

def transform_transaction_gold(df:DataFrame)->DataFrame:
    return df.withColumn("transaction_date",to_date(col("transaction_timestamp")))\
.withColumn("transaction_hour",hour(col("transaction_timestamp")))\
.withColumn("amount_band",when(col("amount")<1000,"LOW").when(col("amount")<10000,"MEDIUM").otherwise("HIGH"))\
.withColumn("is_fraud",col("fraud_flag")=="Y")\
.withColumn("is_successful",col("status")=="SUCCESS")
