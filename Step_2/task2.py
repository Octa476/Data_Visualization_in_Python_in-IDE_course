import pandas as pd

# Read the "gross-domestic-product-june-2024-quarter-visualisation.csv" file using pandas.
df1 = pd.read_csv('gross-domestic-product-june-2024-quarter-visualisation.csv')
df2 = df1

# TO DO: 
# 1) Eliminate all the rows from the dataset that have the field "Description" filled with the
# string "Agriculture" and print the DataFrame to stdout.
# 2) Eliminate all the rows from the initial dataset whose "Weight" is less than 0.01 and print the
# DataFrame to stdout   

# Read the "serious-injury-outcome-indicators-2000-2022.csv" file using pandas.
df1 = pd.read_csv('serious-injury-outcome-indicators-2000-2022.csv')
df2 = df1

# TO DO:
# 1) Eliminate all the "Fatal" injuries from the dataset and print the DataFrame to stdout.
# 2) Eliminate all the injuries that aren't recorded during the year 2004 and print the DataFrame to stdout.
