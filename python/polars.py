def get_value_percentage(df, col_name):

    # load the libraries
    import polars as pl

    # compute the percentage of the unique values
    perc_values = df[col_name].value_counts(sort=True).select(
    pl.col(col_name),
    pl.col('counts'),
    pl.col('counts').apply(lambda x: x/df.shape[0]*100).round(2).alias('perc'))

    # return the df
    return perc_values
