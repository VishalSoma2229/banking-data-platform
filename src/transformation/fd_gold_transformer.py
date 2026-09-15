from pyspark.sql import DataFrame
from pyspark.sql.functions import col,datediff,current_date,when

def transform_fd_gold(df:DataFrame)->DataFrame:
    return df.withColumn("days_to_maturity",datediff(col("maturity_date"),current_date()))\
.withColumn("maturity_bucket",when(col("days_to_maturity")<0,"MATURED").when(col("days_to_maturity")<=90,"MATURING_90_DAYS").otherwise("ACTIVE_TERM"))\
.withColumn("estimated_interest",col("deposit_amount")*col("interest_rate")/100)
