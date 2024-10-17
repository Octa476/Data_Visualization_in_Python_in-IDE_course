import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Read the .csv file using pandas.
df = pd.read_csv('serious-injury-outcome-indicators-2000-2022.csv')

x='Severity'
hue='Cause'
# Create the countplot where the x axis is the platform and the y axis represents the number of
# games for every genre. 
sns.countplot(x=x, hue=hue, data=df, native_scale=True)

print(df)
print(x)
print(hue)

# Show the plot.
plt.show()