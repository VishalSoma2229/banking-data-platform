from src.common.logger import logger
from src.common.spark_session import create_spark_session
from src.config import pipeline_config as config

from src.ingestion.transaction_reader import read_transaction
from src.ingestion.bronze_reader import read_bronze
from src.transformation.transaction_transformer import transform_transaction
from src.transformation.transaction_gold_transformer import transform_transaction_gold
from src.validations.transaction_validator import validate_transaction
from src.writers.bronze_writer import write_bronze
from src.writers.silver_writer import write_silver
from src.writers.gold_writer import write_gold
from src.writers.rejected_writer import write_rejected


def run_transaction_bronze():
    spark = create_spark_session("transaction Bronze Pipeline")
    try:
        df = read_transaction(spark, config.TRANSACTION_SOURCE_PATH)
        write_bronze(df, config.TRANSACTION_BRONZE_PATH)
    except Exception:
        logger.exception("transaction Bronze failed")
        raise
    finally:
        spark.stop()


def run_transaction_silver():
    spark = create_spark_session("transaction Silver Pipeline")
    try:
        df = read_bronze(spark, config.TRANSACTION_BRONZE_PATH)
        df = transform_transaction(df)
        valid, invalid = validate_transaction(df)
        write_silver(valid, config.TRANSACTION_SILVER_PATH)
        write_rejected(invalid, config.TRANSACTION_REJECTED_PATH)
    except Exception:
        logger.exception("transaction Silver failed")
        raise
    finally:
        spark.stop()


def run_transaction_gold():
    spark = create_spark_session("transaction Gold Pipeline")
    try:
        df = read_bronze(spark, config.TRANSACTION_SILVER_PATH)
        df = transform_transaction_gold(df)
        write_gold(df, config.TRANSACTION_GOLD_PATH)
    except Exception:
        logger.exception("transaction Gold failed")
        raise
    finally:
        spark.stop()
