# load the libraries
import pyspark.sql.functions as f
from pyspark.sql.window import Window

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
DROP TABLE IF EXISTS db_name.table_name;
CREATE TABLE db_name.table_name USING DELTA LOCATION 'delta_table_path'

# PROCESSING

# transform a column into a list
list_ids = s_df.select("id").rdd.flatMap(lambda x: x).collect()

# get the latest record for each group
windowOrder = Window \
    .partitionBy("grp_var1", "grp_var2") \
    .orderBy(f.col("datetime_col").desc())

s_df = (
    s_df
    .withColumn("row", f.row_number().over(windowOrder)) 
    .filter(f.col("row") == 1).drop("row")
)

# ANALYSE

# get the min or max of a column
min_value = s_df.select(f.min(f.col("column_name"))).collect()[0][0]
min_value = s_df.select(f.max(f.col("column_name"))).collect()[0][0]
