from src.common.logger import logger
from src.common.spark_session import create_spark_session
from src.config import pipeline_config as config

from src.ingestion.fd_reader import read_fd
from src.ingestion.bronze_reader import read_bronze
from src.transformation.fd_transformer import transform_fd
from src.transformation.fd_gold_transformer import transform_fd_gold
from src.validations.fd_validator import validate_fd
from src.writers.bronze_writer import write_bronze
from src.writers.silver_writer import write_silver
from src.writers.gold_writer import write_gold
from src.writers.rejected_writer import write_rejected


def run_fd_bronze():
    spark = create_spark_session("fd Bronze Pipeline")
    try:
        df = read_fd(spark, config.FD_SOURCE_PATH)
        write_bronze(df, config.FD_BRONZE_PATH)
    except Exception:
        logger.exception("fd Bronze failed")
        raise
    finally:
        spark.stop()


def run_fd_silver():
    spark = create_spark_session("fd Silver Pipeline")
    try:
        df = read_bronze(spark, config.FD_BRONZE_PATH)
        df = transform_fd(df)
        valid, invalid = validate_fd(df)
        write_silver(valid, config.FD_SILVER_PATH)
        write_rejected(invalid, config.FD_REJECTED_PATH)
    except Exception:
        logger.exception("fd Silver failed")
        raise
    finally:
        spark.stop()


def run_fd_gold():
    spark = create_spark_session("fd Gold Pipeline")
    try:
        df = read_bronze(spark, config.FD_SILVER_PATH)
        df = transform_fd_gold(df)
        write_gold(df, config.FD_GOLD_PATH)
    except Exception:
        logger.exception("fd Gold failed")
        raise
    finally:
        spark.stop()
