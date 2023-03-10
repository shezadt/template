# load the libraries
import pyspark.sql.functions as f
from pyspark.sql.window import Window
from pyspark.sql.types import TimestampType, StringType

# SYSTEM

# get the notebook directory path
directory_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()

# CONNECTION / READING

# connect to postgre sql server
source_data = (
    spark.read.format("jdbc")
    .option("url", "jdbc:postgresql://xx.xx.xx.xx:xxxx/db_name")
    .option("dbtable", "table_name")
    .option("user", "xx")
    .option("password", "xx")
    .option("driver", "org.postgresql.Driver")
    .load()
)

# read delta table
source_data = spark.read.load(delta_path)

# read parquet file
source_data = spark.read.parquet(parquet_path)

# read csv file
source_data = spark.read.option("header", "true").csv(csv_path)

# SQL

# transform a sql query into a spark df
results = sqlContext.sql('''SELECT * FROM xxx''')

# create a view from a spark df
s_df.createOrReplaceTempView("view_name")

# create a view in the hive metastore
%sql
CREATE DATABASE IF NOT EXISTS db_name;
DROP TABLE IF EXISTS db_name.table_name;
CREATE TABLE db_name.table_name USING DELTA LOCATION 'delta_table_path'
CREATE TABLE IF NOT EXISTS db_name.table_name USING DELTA LOCATION 'delta_table_path'
spark.sql(
    f"""CREATE TABLE IF NOT EXISTS db_name.table_name USING PARQUET LOCATION '{python_path}'"""
)

# PROCESSING

# transform a column into a list
list_ids = s_df.select("id").rdd.flatMap(lambda x: x).collect()

# create a new column based on condition
s_df = s_df.withColumn(
    "new_column",
    f.when(f.col("colA") == "Cond1", f.col("colB")).otherwise(f.col("colC"))
)

# get the latest record for each group
windowOrder = Window \
    .partitionBy("grp_var1", "grp_var2") \
    .orderBy(f.col("datetime_col").desc())

s_df = (
    s_df
    .withColumn("row", f.row_number().over(windowOrder)) 
    .filter(f.col("row") == 1).drop("row")
)

# use a predefined list as input of an udf function
my_function_udf = f.udf(lambda x: my_function(x, predefined_list), TimestampType())

# remove a pattern from a string column
s_df = (
    s_df.withColumn(f.col("string_col"), f.f.regexp_replace(f.col("string_col"), "pattern_to_remove", "replacement"))
)

# ANALYSE

# get the min or max of a column
min_value = s_df.select(f.min(f.col("column_name"))).collect()[0][0]
min_value = s_df.select(f.max(f.col("column_name"))).collect()[0][0]
