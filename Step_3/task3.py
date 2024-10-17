# Import the modules needed.
import pandas as pd

# Read the .csv file using pandas.
df = pd.read_csv('environmental-tax-account-1999-2022.csv')

# TO DO: 
# Apply a category for the 'Industry_desc' field.
# The category is the sorted unique items of the field.

# TO DO:
# Apply a category for the 'data_value' field on the same DataFrame(df).
# The category is the reversed sorted unique items of the field.

print(df['Industry_desc'].cat.categories)
print(df['data_value'].cat.categories)