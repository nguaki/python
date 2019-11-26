import pandas as pd
#import matplotlib  as plot

df = pd.read_csv("weather_by_cities.csv")

g = df.groupby("city")

#%matplotlib inline
g.plot()