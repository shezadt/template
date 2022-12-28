# load the libraries
import pandas as pd
import numpy as np
from datetime import datetime, timedelta, date

# initialize a dataframe
df = pd.DataFrame({'num_legs': [2, 4, 4, 6, np.NaN],
                   'num_wings': [2, 0, 0, 0, 7]})

# return null data
null_data = df[df.isnull().any(axis=1)]

# get unique values of a column
df['num_wings'].value_counts()

# get today date
today_date = date.today()

# minus days from a date, e.g. 3
start_date = today_date - timedelta(days=3)

# replace the day by another day, e.g. 1
date_replaced = today_date.replace(day=1)
