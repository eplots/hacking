#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('network_traffic.csv')
df.head(5)

# We need to use Pandas count function on the dataframe
# For example: dataframe.count()

print(df.count())
