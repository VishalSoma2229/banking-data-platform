from src.common.logger import logger
from src.common.spark_session import create_spark_session
from src.config import pipeline_config as config

from src.ingestion.card_reader import read_card
from src.ingestion.bronze_reader import read_bronze
from src.transformation.card_transformer import transform_card
from src.transformation.card_gold_transformer import transform_card_gold
from src.validations.card_validator import validate_card
from src.writers.bronze_writer import write_bronze
from src.writers.silver_writer import write_silver
from src.writers.gold_writer import write_gold
from src.writers.rejected_writer import write_rejected


def run_card_bronze():
    spark = create_spark_session("card Bronze Pipeline")
    try:
        df = read_card(spark, config.CARD_SOURCE_PATH)
        write_bronze(df, config.CARD_BRONZE_PATH)
    except Exception:
        logger.exception("card Bronze failed")
        raise
    finally:
        spark.stop()


def run_card_silver():
    spark = create_spark_session("card Silver Pipeline")
    try:
        df = read_bronze(spark, config.CARD_BRONZE_PATH)
        df = transform_card(df)
        valid, invalid = validate_card(df)
        write_silver(valid, config.CARD_SILVER_PATH)
        write_rejected(invalid, config.CARD_REJECTED_PATH)
    except Exception:
        logger.exception("card Silver failed")
        raise
    finally:
        spark.stop()


def run_card_gold():
    spark = create_spark_session("card Gold Pipeline")
    try:
        df = read_bronze(spark, config.CARD_SILVER_PATH)
        df = transform_card_gold(df)
        write_gold(df, config.CARD_GOLD_PATH)
    except Exception:
        logger.exception("card Gold failed")
        raise
    finally:
        spark.stop()
