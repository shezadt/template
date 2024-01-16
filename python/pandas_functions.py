def convert_column_to_string_sql(df, column_name):
    """Convert a pandas column into a string that can be used for SQL queries.

    Args:
        df (dataframe): The input dataframe
        column_name (str): The name of the column

    Returns:
        result (str): The string for SQL queries
    """
    result = "(" + df[column_name].apply(lambda x: f"'{x}'").str.cat(sep=",") + ")"

    return result
