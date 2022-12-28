# load the libraries
import pyspark.sql.functions as f

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

# PROCESSING

# transform a column into a list
list_ids = s_df.select("id").rdd.flatMap(lambda x: x).collect()
