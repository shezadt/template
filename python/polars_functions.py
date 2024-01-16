# function to get percentage of values of a column
def get_value_percentage(df, col_name, digits=2):

  """Get the percentage of values by group in a polars df

    Args:
        df (dataframe): The input dataframe
        col_name (str): The name of the column

    Returns:
        perc_values (dataframe): The percentage calculated
    """

    # load the libraries
    import polars as pl

    # compute the percentage of the unique values
    perc_values = df[col_name].value_counts(sort=True).select(
    pl.col(col_name),
    pl.col('counts'),
    pl.col('counts').apply(lambda x: x/df.shape[0]*100).round(digits).alias('perc'))

    # return the df
    return perc_values
