from pyspark.sql import DataFrame
from pyspark.sql.functions import col,lit,when

def validate_fd(df:DataFrame):
    v=df.withColumn("rejection_reason",
        when(col("fd_id").isNull(),"FD ID is NULL")
.when(col("customer_id").isNull(),"Customer ID is NULL")
.when(col("deposit_amount").isNull(),"Deposit Amount is NULL")
.when(col("deposit_amount")<=0,"Deposit Amount must be positive")
.when(col("interest_rate").isNull(),"Interest Rate is NULL")
.when(col("interest_rate")<0,"Negative Interest Rate")
.when(col("maturity_date").isNull(),"Maturity Date is NULL")
        .otherwise(lit(None)))
    valid=v.filter(col("rejection_reason").isNull()).drop("rejection_reason")
    invalid=v.filter(col("rejection_reason").isNotNull())
    return valid,invalid
