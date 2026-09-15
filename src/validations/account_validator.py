from pyspark.sql import DataFrame
from pyspark.sql.functions import col,lit,when

def validate_account(df:DataFrame):
    v=df.withColumn("rejection_reason",
        when(col("account_id").isNull(),"Account ID is NULL")
.when(col("customer_id").isNull(),"Customer ID is NULL")
.when(col("branch_id").isNull(),"Branch ID is NULL")
.when(col("account_number").isNull(),"Account Number is NULL")
.when(col("balance")<0,"Negative Balance")
.when(col("opened_date").isNull(),"Opened Date is NULL")
        .otherwise(lit(None)))
    valid=v.filter(col("rejection_reason").isNull()).drop("rejection_reason")
    invalid=v.filter(col("rejection_reason").isNotNull())
    return valid,invalid
