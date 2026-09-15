from pyspark.sql import DataFrame
from pyspark.sql.functions import col,lit,when

def validate_card(df:DataFrame):
    v=df.withColumn("rejection_reason",
        when(col("card_id").isNull(),"Card ID is NULL")
.when(col("account_id").isNull(),"Account ID is NULL")
.when(col("issue_date").isNull(),"Issue Date is NULL")
.when(col("expiry_date").isNull(),"Expiry Date is NULL")
.when(col("expiry_date")<=col("issue_date"),"Expiry Date must be after Issue Date")
        .otherwise(lit(None)))
    valid=v.filter(col("rejection_reason").isNull()).drop("rejection_reason")
    invalid=v.filter(col("rejection_reason").isNotNull())
    return valid,invalid
