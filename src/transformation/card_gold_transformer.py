from pyspark.sql import DataFrame
from pyspark.sql.functions import col,datediff,current_date,when

def transform_card_gold(df:DataFrame)->DataFrame:
    return df.withColumn("card_age_days",datediff(current_date(),col("issue_date")))\
.withColumn("days_to_expiry",datediff(col("expiry_date"),current_date()))\
.withColumn("expiry_bucket",when(col("days_to_expiry")<0,"EXPIRED").when(col("days_to_expiry")<=90,"EXPIRING_90_DAYS").otherwise("VALID"))
