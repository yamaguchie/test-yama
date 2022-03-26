# Databricks notebook source
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
app_name = spark.conf.get("spark.app.name")
if app_name == 'Databricks Sahell':
  print("Databricks Notebook Execute")
  %run "../../test_yama/jobs/sample/entrypoint"
else:
  import os
  #from test_yama.jobs.sample.entrypoint import SampleJob

# COMMAND ----------

# MAGIC %whos
