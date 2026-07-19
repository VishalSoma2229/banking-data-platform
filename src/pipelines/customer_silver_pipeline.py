from src.config.pipeline_config import (
    CUSTOMER_BRONZE_PATH,
    CUSTOMER_SILVER_PATH,
    CUSTOMER_REJECTED_PATH
)
from src.common.logger import logger

from src.ingestion.bronze_reader import read_bronze
from src.transformation.customer_transformer import transform_customer
from src.validations.customer_validator import validate_customer

from src.writers.silver_writer import write_silver
from src.writers.rejected_writer import write_rejected

from src.common.spark_session import create_spark_session

def run_customer_silver():

    logger.info("=" * 60)
    logger.info("Starting Customer Silver Pipeline")
    logger.info("=" * 60)

    spark = create_spark_session("Customer Silver Pipeline")

    try:
        # Read Bronze
        customer_df = read_bronze(
            spark,
            CUSTOMER_BRONZE_PATH
        )

        logger.info(f"Bronze Records : {customer_df.count()}")

        # Transform
        customer_df = transform_customer(customer_df)

        # Validate
        valid_df, invalid_df = validate_customer(customer_df)

        logger.info(f"Valid Records   : {valid_df.count()}")
        logger.info(f"Invalid Records : {invalid_df.count()}")

        # Write Silver
        write_silver(
            valid_df,
            CUSTOMER_SILVER_PATH
        )

        logger.info("Silver Layer Written Successfully")

        # Write Rejected
        write_rejected(
            invalid_df,
            CUSTOMER_REJECTED_PATH
        )

        logger.info("Rejected Records Written Successfully")

    except Exception as e:
        logger.info(f"Customer Silver Pipeline Failed: {e}")
        raise

    finally:
        spark.stop()
        logger.info("Spark Session Stopped")

    logger.info("Customer Silver Pipeline Completed")
    logger.info("=" * 60)