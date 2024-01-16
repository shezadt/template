# load the libraries
import polars as pl

# add prefix to column names
df_new = df.select([pl.col(c).alias("prefix_" + c) for c in df.columns])
