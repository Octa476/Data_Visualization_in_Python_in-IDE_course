# Reference Solution

import pandas as pd

# Read the "gross-domestic-product-june-2024-quarter-visualisation.csv" file using pandas.
df1 = pd.read_csv('gross-domestic-product-june-2024-quarter-visualisation.csv')

df2 = df1
# Eliminate all the rows from the dataset that have the field "Description" filled with the
# string "Agriculture".  
for row in df1.index:
  if df1.loc[row, "Description"] == "Agriculture":
    df1.drop(row, inplace = True)

print(df1)

df2 = df1
# Eliminate all the rows from the dataset whose "Weight" is less than 0.01.
for row in df2.index:
  if float(df2.loc[row, "Weight"]) < 0.01:
    df2.drop(row, inplace = True)

print(df2)

# Read the "serious-injury-outcome-indicators-2000-2022.csv" file using pandas.
df1 = pd.read_csv('serious-injury-outcome-indicators-2000-2022.csv')

df2 = df1
# Eliminate all the "Fatal" injuries from the dataset.
for row in df1.index:
  if df1.loc[row, "Severity"] == "Fatal":
    df1.drop(row, inplace = True)

print(df1)

# Eliminate all the injuries that aren't recorded during the year 2004.
for row in df2.index:
  if int(df2.loc[row, "Period"].split("-")[0]) == 2004:
    df2.drop(row, inplace = True)

print(df2)
