from pyspark.sql import DataFrame
from pyspark.sql.functions import col,datediff,current_date,when

def transform_account_gold(df:DataFrame)->DataFrame:
    return df.withColumn("account_age_days",datediff(current_date(),col("opened_date")))\
.withColumn("balance_band",when(col("balance")<100000,"LOW").when(col("balance")<1000000,"MEDIUM").otherwise("HIGH"))\
.withColumn("is_active",col("account_status")=="ACTIVE")
