from src.common.logger import logger
from src.common.spark_session import create_spark_session
from src.config import pipeline_config as config

from src.ingestion.branch_reader import read_branch
from src.ingestion.bronze_reader import read_bronze
from src.transformation.branch_transformer import transform_branch
from src.transformation.branch_gold_transformer import transform_branch_gold
from src.validations.branch_validator import validate_branch
from src.writers.bronze_writer import write_bronze
from src.writers.silver_writer import write_silver
from src.writers.gold_writer import write_gold
from src.writers.rejected_writer import write_rejected


def run_branch_bronze():
    spark = create_spark_session("branch Bronze Pipeline")
    try:
        df = read_branch(spark, config.BRANCH_SOURCE_PATH)
        write_bronze(df, config.BRANCH_BRONZE_PATH)
    except Exception:
        logger.exception("branch Bronze failed")
        raise
    finally:
        spark.stop()


def run_branch_silver():
    spark = create_spark_session("branch Silver Pipeline")
    try:
        df = read_bronze(spark, config.BRANCH_BRONZE_PATH)
        df = transform_branch(df)
        valid, invalid = validate_branch(df)
        write_silver(valid, config.BRANCH_SILVER_PATH)
        write_rejected(invalid, config.BRANCH_REJECTED_PATH)
    except Exception:
        logger.exception("branch Silver failed")
        raise
    finally:
        spark.stop()


def run_branch_gold():
    spark = create_spark_session("branch Gold Pipeline")
    try:
        df = read_bronze(spark, config.BRANCH_SILVER_PATH)
        df = transform_branch_gold(df)
        write_gold(df, config.BRANCH_GOLD_PATH)
    except Exception:
        logger.exception("branch Gold failed")
        raise
    finally:
        spark.stop()
