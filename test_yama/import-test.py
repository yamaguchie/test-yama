# Databricks notebook source
try:
  from test_yama.jobs.sample.entrypoint import SampleJob
except:
  pass
  %run "../../test_yama/jobs/sample/entrypoint"
