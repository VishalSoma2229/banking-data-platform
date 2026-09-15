from pyspark.sql import DataFrame
from pyspark.sql.functions import col,round,when,pow

def transform_loan_gold(df:DataFrame)->DataFrame:
    return df.withColumn("monthly_rate",col("interest_rate")/1200)\
.withColumn("monthly_emi",when(col("monthly_rate")==0,col("principal")/col("tenure_months"))\
.otherwise(col("principal")*col("monthly_rate")*pow(1+col("monthly_rate"),col("tenure_months"))/(pow(1+col("monthly_rate"),col("tenure_months"))-1)))\
.withColumn("estimated_total_repayment",round(col("monthly_emi")*col("tenure_months"),2))\
.withColumn("estimated_total_interest",round(col("estimated_total_repayment")-col("principal"),2))\
.drop("monthly_rate")
