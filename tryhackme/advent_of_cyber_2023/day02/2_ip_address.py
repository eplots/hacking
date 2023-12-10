#!/usr/bin/python3
import pandas as pd

df = pd.read_csv('network_traffic.csv')
df.head(5)

# We need to perform a groupby with Pandas size function the "Source" and "Destination" columns.
# For example: dataframe.groupby(['ColumnName']).size()

print(df.groupby(['Source']).size().sort_values(ascending=False))
