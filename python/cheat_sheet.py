# Load the libraries
import pandas as pd
import numpy as np

# Initialize a dataframe
df = pd.DataFrame({'num_legs': [2, 4, 4, 6, np.NaN],
                   'num_wings': [2, 0, 0, 0, 7]})

# Return null data
null_data = df[df.isnull().any(axis=1)]

# Get unique values of a column
df['num_wings'].value_counts()