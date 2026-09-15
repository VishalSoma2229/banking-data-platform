from pyspark.sql import SparkSession,DataFrame
from src.models.branch_schema import branch_schema

def read_branch(spark:SparkSession,file_path:str)->DataFrame:
    return spark.read.option("header",True).option("timestampFormat","yyyy-MM-dd HH:mm:ss.SSSSSS").schema(branch_schema).csv(file_path)
