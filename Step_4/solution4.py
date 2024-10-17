# Reference Solution

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Read the .csv file using pandas.
df = pd.read_csv('serious-injury-outcome-indicators-2000-2022.csv')

x='Severity'
hue='Cause'

# Create the countplot where the x axis is the "Severity" and the y axis represents the number of
# injuries per every "Cause". 
sns.countplot(x=x, hue=hue, data=df, native_scale=True)

# Show the plot.
plt.show()

# Printing done for the checker.
print(df)
print(x)
print(hue)
