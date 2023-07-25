# load the libraries
import polars as pl

# add prefix to column names
df_new = df.select([pl.col(c).alias("prefix_" + c) for c in df.columns])

# function to get percentage of values of a column
def get_value_percentage(df, col_name, digits=2):

    # load the libraries
    import polars as pl

    # compute the percentage of the unique values
    perc_values = df[col_name].value_counts(sort=True).select(
    pl.col(col_name),
    pl.col('counts'),
    pl.col('counts').apply(lambda x: x/df.shape[0]*100).round(digits).alias('perc'))

    # return the df
    return perc_values
