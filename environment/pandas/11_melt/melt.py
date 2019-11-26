import pandas as pd
df = pd.read_csv("weather.csv")
print(df)

#Not sure when would you need to use melt.
melted = pd.melt(df, id_vars=["day"], var_name='city', value_name='temperature')
print(melted)