# Reference Solution

# Import the modules needed.
import pandas as pd

# Read the .csv file using pandas.
df = pd.read_csv('environmental-tax-account-1999-2022.csv')

# Create a list of sorted Industry_desc.
unique = df['Industry_desc'].unique()
order_Industry_desc = [str(x) for x in unique]
order_Industry_desc.sort()

# Apply the "order_Industry_desc" order to the 'Industry_desc' field.
df['Industry_desc'] = pd.Categorical(df['Industry_desc'], categories=order_Industry_desc, ordered=True)

df['data_value'] = df['data_value'].fillna(0)
# Create a list of sorted "data_value" in reverse order.
order_data_value = sorted(df['data_value'].unique(), reverse=True)

# Apply the "order_data_value" order to the 'data_value' field.
df['data_value'] = pd.Categorical(df['data_value'], categories=order_data_value, ordered=True)

print(df['Industry_desc'].cat.categories)
print(df['data_value'].cat.categories)

# Now the two fields have a defined category atribute 