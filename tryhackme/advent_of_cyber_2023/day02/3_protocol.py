import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('network_traffic.csv')
df.head(5)

print(df['Protocol'].value_counts())
