import pandas as pd
import numpy as np

#df = pd.read_csv("weather.csv",parse_dates=['date'])
#Watch out for hidden characters in textfile
df = pd.read_csv("weather.csv")
print (df)

print (type(df.date[0]))

#Now, change the perspective of the table by using pivot
#Make index city(rows) and date columns.
print('-------------------------------------------------')
print('pivot city to index and pivot date to columns')
print(df.pivot(index='city',columns='date'))


#Now show just humidity 
print('-------------------------------------------------')
print('pivot city to index and pivot date to columns show humidity')
print(df.pivot(index='city',columns='date',values="humidity"))

print('-------------------------------------------------')
print('pivot date to index and pivot city to columns')
print(df.pivot(index='date',columns='city'))

print('-------------------------------------------------')
print('pivot humidity to index and pivot city to columns')
print(df.pivot(index='humidity',columns='city'))

df = pd.read_csv("weather2.csv")
print('-------------------------------------------------')
print('Reading weather2.csv')
print(df)

print('-------------------------------------------------')
print('pivot city to index and pivot date to columns')
#Note that if there are multiple value on a same date, there will be average.
print(df.pivot_table(index="city",columns="date"))

print('-------------------------------------------------')
print('pivot city to index and pivot date to columns assign aggfunc')
#aggfunc=np.sum will aggregate all values and create a summary line.
print(df.pivot_table(index="city",columns="date", margins=True,aggfunc=np.sum))

df = pd.read_csv("weather3.csv")
print('-------------------------------------------------')
print('Reading weather3.csv')
print(df)

#Causing this error messages
#  File "pivot.py", line 35, in <module>
#    print(df.pivot_table(index=pd.Grouper(freq='M',key='date'),columns='city'))
#  File "/home/ubuntu/anaconda/lib/python2.7/site-packages/pandas/tools/pivot.py", line 95, in pivot_table
#    values = list(data.columns.drop(keys))
#  File "/home/ubuntu/anaconda/lib/python2.7/site-packages/pandas/core/index.py", line 2570, in drop
#    raise ValueError('labels %s not contained in axis' % labels[mask])
#ValueError: labels [<pandas.tseries.resample.TimeGrouper object at 0x7ff991163bd0>] not contained in axis

df['date'] = pd.to_datetime(df['date'])
print(df.pivot_table(index=pd.Grouper(freq='M',key='date'),columns='city'))


