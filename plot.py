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

# Apply the "order_genre" order to the DataFrame(df).  
df['genre'] = pd.Categorical(df['genre'], categories=order_genre, ordered=True)

# Create the countplot where the x axis is the platform and the y axis represents the number of
# games for every genre. 
sns.countplot(x='platform', hue='genre', data=df, native_scale=True)

# Show the plot.
plt.show()
