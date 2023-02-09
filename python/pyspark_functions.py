from pyspark.sql.functions import array, col, explode, lit, struct
from pyspark.sql import DataFrame
from typing import Iterable

# Function to convert a wide dataframe into a long data frame
def melt_df(
    df: DataFrame,
    id_vars: Iterable[str],
    value_vars: Iterable[str],
    var_name: str = "variable",
    value_name: str = "value",
) -> DataFrame:
    """Convert a wide data frame to long

    Args:
        df (dataframe): The input dataframe
        id_vars (Iterable[str]): list of id vars
        value_vars (Iterable[str]): list of value vars
        var_name (str): name of the variable column
        value_name (str): name of the value column

    Returns:
        df: The output long dataframe
    """

    from pyspark.sql.functions import array, col, explode, lit, struct
    from pyspark.sql import DataFrame
    from typing import Iterable

    # Create array<struct<variable: str, value: ...>>
    _vars_and_vals = array(
        *(struct(lit(c).alias(var_name), col(c).alias(value_name)) for c in value_vars)
    )

    # Add to the DataFrame and explode
    _tmp = df.withColumn("_vars_and_vals", explode(_vars_and_vals))

    cols = id_vars + [col("_vars_and_vals")[x].alias(x) for x in [var_name, value_name]]
    return _tmp.select(*cols)
