from pyspark.sql import DataFrame
from pyspark.sql.functions import col,trim,upper,initcap,current_timestamp

def transform_branch(df:DataFrame)->DataFrame:
    return (df.dropDuplicates(["branch_id"])
.withColumn("branch_name",initcap(trim(col("branch_name"))))
.withColumn("ifsc_code",upper(trim(col("ifsc_code"))))
.withColumn("city",initcap(trim(col("city"))))
.withColumn("state",initcap(trim(col("state"))))
.withColumn("region",upper(trim(col("region"))))
.withColumn("ingestion_timestamp",current_timestamp()))
