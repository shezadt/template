# read data from databricks in R
raw_data = as_tibble(SparkR::collect(SparkR::sql("FROM table_name SELECT *")))
