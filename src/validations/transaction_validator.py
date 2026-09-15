from pyspark.sql import DataFrame
from pyspark.sql.functions import col,lit,when

def validate_transaction(df:DataFrame):
    v=df.withColumn("rejection_reason",
        when(col("transaction_id").isNull(),"Transaction ID is NULL")
.when(col("account_id").isNull(),"Account ID is NULL")
.when(col("transaction_timestamp").isNull(),"Transaction Timestamp is NULL")
.when(col("transaction_type").isNull(),"Transaction Type is NULL")
.when(col("amount").isNull(),"Amount is NULL")
.when(col("amount")<=0,"Amount must be positive")
.when(col("currency").isNull(),"Currency is NULL")
.when(col("status").isNull(),"Status is NULL")
.when(col("fraud_flag").isNull(),"Fraud Flag is NULL")
        .otherwise(lit(None)))
    valid=v.filter(col("rejection_reason").isNull()).drop("rejection_reason")
    invalid=v.filter(col("rejection_reason").isNotNull())
    return valid,invalid
