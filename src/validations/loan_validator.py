from pyspark.sql import DataFrame
from pyspark.sql.functions import col,lit,when

def validate_loan(df:DataFrame):
    v=df.withColumn("rejection_reason",
        when(col("loan_id").isNull(),"Loan ID is NULL")
.when(col("customer_id").isNull(),"Customer ID is NULL")
.when(col("principal").isNull(),"Principal is NULL")
.when(col("principal")<=0,"Principal must be positive")
.when(col("interest_rate").isNull(),"Interest Rate is NULL")
.when(col("interest_rate")<0,"Negative Interest Rate")
.when(col("tenure_months").isNull(),"Tenure is NULL")
.when(col("tenure_months")<=0,"Tenure must be positive")
        .otherwise(lit(None)))
    valid=v.filter(col("rejection_reason").isNull()).drop("rejection_reason")
    invalid=v.filter(col("rejection_reason").isNotNull())
    return valid,invalid
