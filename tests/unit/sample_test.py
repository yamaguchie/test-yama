# Databricks notebook source
## Databricks notebook source
import unittest
import tempfile
import os
import shutil
  
# from test_yama.jobs.sample.entrypoint import SampleJob
from pyspark.sql import SparkSession
from unittest.mock import MagicMock

# DatabricksNotebook上では当該SparkSession、それ以外の場合はlocalモードを想定。
spark = SparkSession.builder.getOrCreate()
app_name = spark.conf.get("spark.app.name")
if app_name == 'Databricks Shell':
  print("Databricks Notebook Execute")
  %run "../../test_yama/jobs/sample/entrypoint"
  #%run "./mymodule/hoge"
else:
  from test_yama.jobs.sample.entrypoint import SampleJob

class SampleJobUnitTest(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory().name
        self.spark = SparkSession.builder.master("local[1]").getOrCreate()
        self.test_config = {
            "output_format": "parquet",
            "output_path": os.path.join(self.test_dir, "output"),
        }
        self.job = SampleJob(spark=self.spark, init_conf=self.test_config)

    def test_sample(self):
        # feel free to add new methods to this magic mock to mock some particular functionality
        self.job.dbutils = MagicMock()

        self.job.launch()

        output_count = (
            self.spark.read.format(self.test_config["output_format"])
            .load(self.test_config["output_path"])
            .count()
        )

        self.assertGreater(output_count, 0)

    def tearDown(self):
        shutil.rmtree(self.test_dir)


if __name__ == "__main__":
    tmp=SampleJobUnitTest()
    tmp.setUp()
    tmp.test_sample()
    #unittest.main()

# COMMAND ----------

# MAGIC %whos

# COMMAND ----------

# MAGIC %run "../../test_yama/jobs/sample/entrypoint"

# COMMAND ----------

# MAGIC %whos
