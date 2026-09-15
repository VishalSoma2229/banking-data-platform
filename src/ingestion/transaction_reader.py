from pyspark.sql import SparkSession,DataFrame
from src.models.transaction_schema import transaction_schema

def read_transaction(spark:SparkSession,file_path:str)->DataFrame:
    return spark.read.option("header",True).option("timestampFormat","yyyy-MM-dd HH:mm:ss.SSSSSS").schema(transaction_schema).csv(file_path)
