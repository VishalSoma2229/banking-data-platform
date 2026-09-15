from pyspark.sql import DataFrame
from pyspark.sql.functions import col,datediff,current_date,concat_ws

def transform_branch_gold(df:DataFrame)->DataFrame:
    return df.withColumn("branch_age_days",datediff(current_date(),col("opening_date")))\
.withColumn("branch_label",concat_ws(" - ",col("branch_id"),col("branch_name")))
