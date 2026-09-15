from pyspark.sql import SparkSession,DataFrame
from src.models.account_schema import account_schema

def read_account(spark:SparkSession,file_path:str)->DataFrame:
    return spark.read.option("header",True).option("timestampFormat","yyyy-MM-dd HH:mm:ss.SSSSSS").schema(account_schema).csv(file_path)
