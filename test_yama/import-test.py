# Databricks notebook source
spark = SparkSession.builder.getOrCreate()
app_name = spark.conf.get("spark.app.name")
if app_name == 'Databricks Shell':
  print("Databricks Notebook Execute")
  %run "../../test_yama/jobs/sample/entrypoint"
else:
  from test_yama.jobs.sample.entrypoint import SampleJob
