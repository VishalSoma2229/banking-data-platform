from pyspark.sql import SparkSession,DataFrame
from src.models.loan_schema import loan_schema

def read_loan(spark:SparkSession,file_path:str)->DataFrame:
    return spark.read.option("header",True).option("timestampFormat","yyyy-MM-dd HH:mm:ss.SSSSSS").schema(loan_schema).csv(file_path)
