from pyspark.sql import SparkSession

import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

# Stop the old session first
try:
    spark.stop()
except:
    pass
