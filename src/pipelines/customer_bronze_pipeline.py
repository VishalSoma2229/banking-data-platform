from src.config.pipeline_config import (
    CUSTOMER_SOURCE_PATH,
    CUSTOMER_BRONZE_PATH
)

from src.common.logger import logger

from src.ingestion.customer_reader import read_customer
from src.writers.bronze_writer import write_bronze
from src.common.spark_session import create_spark_session


def run_customer_bronze():

    logger.info("=" * 60)
    logger.info("Starting Customer Bronze Pipeline")
    logger.info("=" * 60)

    spark = create_spark_session("Customer Bronze Pipeline")

    try:

        logger.info("1. Spark session created")

        # Read Customer Source Data
        customer_df = read_customer(
            spark,
            CUSTOMER_SOURCE_PATH
        )

        logger.info("2. CSV read completed")

        logger.info("3. Starting count")
        
        logger.info(f"Records Read : {customer_df.count()}")

        customer_df.printSchema()

        customer_df.show(10, truncate=False)

        # Write to Bronze Layer
        write_bronze(
            customer_df,
            CUSTOMER_BRONZE_PATH
        )

        logger.info("Customer Bronze Layer Written Successfully")

    except Exception as e:
        logger.info(f"Customer Bronze Pipeline Failed: {e}")
        raise

    finally:
        spark.stop()
        logger.info("Spark Session Stopped")

    logger.info("Customer Bronze Pipeline Completed")
    logger.info("=" * 60)