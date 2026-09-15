from src.common.logger import logger
from src.common.spark_session import create_spark_session
from src.config import pipeline_config as config

from src.ingestion.loan_reader import read_loan
from src.ingestion.bronze_reader import read_bronze
from src.transformation.loan_transformer import transform_loan
from src.transformation.loan_gold_transformer import transform_loan_gold
from src.validations.loan_validator import validate_loan
from src.writers.bronze_writer import write_bronze
from src.writers.silver_writer import write_silver
from src.writers.gold_writer import write_gold
from src.writers.rejected_writer import write_rejected


def run_loan_bronze():
    spark = create_spark_session("loan Bronze Pipeline")
    try:
        df = read_loan(spark, config.LOAN_SOURCE_PATH)
        write_bronze(df, config.LOAN_BRONZE_PATH)
    except Exception:
        logger.exception("loan Bronze failed")
        raise
    finally:
        spark.stop()


def run_loan_silver():
    spark = create_spark_session("loan Silver Pipeline")
    try:
        df = read_bronze(spark, config.LOAN_BRONZE_PATH)
        df = transform_loan(df)
        valid, invalid = validate_loan(df)
        write_silver(valid, config.LOAN_SILVER_PATH)
        write_rejected(invalid, config.LOAN_REJECTED_PATH)
    except Exception:
        logger.exception("loan Silver failed")
        raise
    finally:
        spark.stop()


def run_loan_gold():
    spark = create_spark_session("loan Gold Pipeline")
    try:
        df = read_bronze(spark, config.LOAN_SILVER_PATH)
        df = transform_loan_gold(df)
        write_gold(df, config.LOAN_GOLD_PATH)
    except Exception:
        logger.exception("loan Gold failed")
        raise
    finally:
        spark.stop()
