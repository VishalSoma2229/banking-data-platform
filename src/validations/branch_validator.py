from pyspark.sql import DataFrame
from pyspark.sql.functions import col,lit,when,length

def validate_branch(df:DataFrame):
    v=df.withColumn("rejection_reason",
        when(col("branch_id").isNull(),"Branch ID is NULL")
.when(col("branch_name").isNull(),"Branch Name is NULL")
.when(col("ifsc_code").isNull(),"IFSC Code is NULL")
.when(length(col("ifsc_code"))!=11,"Invalid IFSC Code")
.when(col("city").isNull(),"City is NULL")
.when(col("opening_date").isNull(),"Opening Date is NULL")
        .otherwise(lit(None)))
    valid=v.filter(col("rejection_reason").isNull()).drop("rejection_reason")
    invalid=v.filter(col("rejection_reason").isNotNull())
    return valid,invalid
