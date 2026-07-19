from src.config.pipeline_config import (
    CUSTOMER_SILVER_PATH,
    CUSTOMER_GOLD_PATH
)
from src.common.logger import logger

from src.ingestion.bronze_reader import read_bronze
from src.transformation.customer_gold_transformer import (
    transform_customer_gold
)
from src.writers.gold_writer import write_gold
from src.common.spark_session import create_spark_session

def run_customer_gold():

    logger.info("=" * 60)
    logger.info("Starting Customer Gold Pipeline")
    logger.info("=" * 60)

    spark = create_spark_session("Customer Gold Pipeline")

    try:
        customer_df = read_bronze(
            spark,
            CUSTOMER_SILVER_PATH
        )

        logger.info(f"Silver Records : {customer_df.count()}")

        customer_df = transform_customer_gold(customer_df)

        customer_df.show(10, truncate=False)

        write_gold(
            customer_df,
            CUSTOMER_GOLD_PATH
        )

        logger.info("Gold Layer Written Successfully")

    except Exception as e:
        logger.info(f"Customer Gold Pipeline Failed: {e}")
        raise

    finally:
        spark.stop()
        logger.info("Spark Session Stopped")

    logger.info("Customer Gold Pipeline Completed")
    logger.info("=" * 60)