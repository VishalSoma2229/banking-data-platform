from src.common.logger import logger
from src.common.spark_session import create_spark_session
from src.config import pipeline_config as config

from src.ingestion.account_reader import read_account
from src.ingestion.bronze_reader import read_bronze
from src.transformation.account_transformer import transform_account
from src.transformation.account_gold_transformer import transform_account_gold
from src.validations.account_validator import validate_account
from src.writers.bronze_writer import write_bronze
from src.writers.silver_writer import write_silver
from src.writers.gold_writer import write_gold
from src.writers.rejected_writer import write_rejected


def run_account_bronze():
    spark = create_spark_session("account Bronze Pipeline")
    try:
        df = read_account(spark, config.ACCOUNT_SOURCE_PATH)
        write_bronze(df, config.ACCOUNT_BRONZE_PATH)
    except Exception:
        logger.exception("account Bronze failed")
        raise
    finally:
        spark.stop()


def run_account_silver():
    spark = create_spark_session("account Silver Pipeline")
    try:
        df = read_bronze(spark, config.ACCOUNT_BRONZE_PATH)
        df = transform_account(df)
        valid, invalid = validate_account(df)
        write_silver(valid, config.ACCOUNT_SILVER_PATH)
        write_rejected(invalid, config.ACCOUNT_REJECTED_PATH)
    except Exception:
        logger.exception("account Silver failed")
        raise
    finally:
        spark.stop()


def run_account_gold():
    spark = create_spark_session("account Gold Pipeline")
    try:
        df = read_bronze(spark, config.ACCOUNT_SILVER_PATH)
        df = transform_account_gold(df)
        write_gold(df, config.ACCOUNT_GOLD_PATH)
    except Exception:
        logger.exception("account Gold failed")
        raise
    finally:
        spark.stop()
