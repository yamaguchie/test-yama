# Databricks notebook source
## Databricks notebook source
import unittest

try:
  from test_yama.jobs.sample.entrypoint import SampleJob
except:
  %run "../../test_yama/jobs/sample/entrypoint"

# COMMAND ----------

# MAGIC %whos

# COMMAND ----------

# MAGIC %run ./moe

# COMMAND ----------

# MAGIC %whos
