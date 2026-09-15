from pyspark.sql import SparkSession,DataFrame
from src.models.card_schema import card_schema

def read_card(spark:SparkSession,file_path:str)->DataFrame:
    return spark.read.option("header",True).option("timestampFormat","yyyy-MM-dd HH:mm:ss.SSSSSS").schema(card_schema).csv(file_path)
