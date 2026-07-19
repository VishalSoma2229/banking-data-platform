import os

import pytest
from pyspark.sql import SparkSession


# Tell Spark which Python executable to use
os.environ["PYSPARK_PYTHON"] = os.sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = os.sys.executable


@pytest.fixture(scope="session")
def spark():

    spark = (
        SparkSession.builder
        .master("local[*]")
        .appName("BankingPipelineTests")
        .getOrCreate()
    )

    yield spark

    spark.stop()