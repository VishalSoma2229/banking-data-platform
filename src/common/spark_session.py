from pyspark.sql import SparkSession

from src.config.storage_config import (
    MINIO_ENDPOINT,
    MINIO_ACCESS_KEY,
    MINIO_SECRET_KEY,
)


def create_spark_session(app_name: str):

    spark = (
        SparkSession.builder
        .appName(app_name)
        .master("local[*]")

        .config(
            "spark.hadoop.fs.s3a.endpoint",
            MINIO_ENDPOINT
        )

        .config(
            "spark.hadoop.fs.s3a.access.key",
            MINIO_ACCESS_KEY
        )

        .config(
            "spark.hadoop.fs.s3a.secret.key",
            MINIO_SECRET_KEY
        )

        .config(
            "spark.hadoop.fs.s3a.aws.credentials.provider",
            "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider"
        )

        .config(
            "spark.hadoop.fs.s3a.endpoint.region",
            "us-east-1"
        )

        .config(
            "spark.hadoop.fs.s3a.path.style.access",
            "true"
        )

        .config(
            "spark.hadoop.fs.s3a.connection.ssl.enabled",
            "false"
        )

        .config(
            "spark.hadoop.fs.s3a.impl",
            "org.apache.hadoop.fs.s3a.S3AFileSystem"
        )

        .config(
            "spark.jars.packages",
            "org.apache.hadoop:hadoop-aws:3.3.4,"
            "com.amazonaws:aws-java-sdk-bundle:1.12.262"
        )

        .config(
            "spark.jars.repositories",
            "https://repo1.maven.org/maven2"
        )

        .getOrCreate()
    )

    return spark