# Reference Solution

# Import the modules needed.
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Read the .csv file using pandas.
df = pd.read_csv('dataset.csv')

# Eliminate all the rows(games) that aren't playable on ["PS4", "XOne", "PC", "WiiU"].  
for row in df.index:
  if df.loc[row, "platform"] not in ["PS4", "XOne", "PC", "WiiU"]:
    df.drop(row, inplace = True)

# Create a list of sorted genres.
order_genre = sorted(df['genre'].unique())
# Create a list with platforms ordered by your preferencies.
order_platform = ["PS4", "XOne", "PC", "WiiU"]

# Apply the "order_genre" order to the DataFrame(df).
df['genre'] = pd.Categorical(df['genre'], categories=order_genre, ordered=True)
# Apply the "order_platform" order to the DataFrame(df).
df['platform'] = pd.Categorical(df['platform'], categories=order_platform, ordered=True)

print(df)
print(df['genre'].cat.categories)
print(df['platform'].cat.categories)
x='platform'
hue='genre'
print(x)
print(hue)

# Create the countplot where the x axis is the platform and the y axis represents the number of
# games for every genre. 
sns.countplot(x=x, hue=hue, data=df, native_scale=True)

# Show the plot.
plt.show()
