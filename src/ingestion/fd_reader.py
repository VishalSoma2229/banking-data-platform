from pyspark.sql import SparkSession,DataFrame
from src.models.fd_schema import fd_schema

def read_fd(spark:SparkSession,file_path:str)->DataFrame:
    return spark.read.option("header",True).option("timestampFormat","yyyy-MM-dd HH:mm:ss.SSSSSS").schema(fd_schema).csv(file_path)
