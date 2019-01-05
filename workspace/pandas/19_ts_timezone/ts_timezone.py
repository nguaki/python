import pandas as pd

#Ignore the top header.
#Make Date Time the index
#Convert string date to object date.
df = pd.read_csv("msft.csv", header=1,index_col='Date Time',parse_dates=True)
print(df)

print(df.index)

#Set timezone 
df.index = df.index.tz_localize(tz='US/Eastern')
print(df)
print(df.index)

df = df.tz_convert('Europe/Berlin')
print(df)

#Create date range with timezone
london = pd.date_range('3/6/2012 00:09:00', periods=10, freq='H',tz='Europe/London')
print(london)

rng = pd.date_range(start="2017-08-22 09:00:00",periods=10, freq='30min')
s = pd.Series(range(10),index=rng)
print(s)

