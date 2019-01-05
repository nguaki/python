import pandas as pd

df = pd.read_csv("aapl_no_dates.csv")
print(df.head())

#Business day only
rng = pd.date_range(start="6/1/2016",end="6/30/2016",freq='B')
print(rng)

#Forces date range to be index
df.set_index(rng, inplace=True)
print(df.head())

#Gets daily index between June 1 to June 30
daily_index = pd.date_range(start="6/1/2016",end="6/30/2016",freq='D')
print(daily_index)

#This function will retrieve the difference between two dau indices
print(daily_index.difference(df.index))

#Since Sat and Sun data are not available, copy Friday's data to Sat and Sun.
print(df.asfreq('D',method='pad'))

#This prints out Sunday data.
print(df.asfreq('W',method='pad'))

#Copies data for hourly basis.
#print(df.asfreq('H',method='pad'))

#Sets hourly indices
rng = pd.date_range('1/1/2011', periods=72, freq='H')
print(rng)

#Generates randome integer from 0,10 for 72 times.
#Index is set time
import numpy as np
ts = pd.Series(np.random.randint(0,10,len(rng)), index=rng)
print(ts.head(20))