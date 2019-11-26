import pandas as pd

#Year
y = pd.Period('2016')
print(y)

#prints out 2016-01-01 00:00:00
print(y.start_time)

#prints out 2016-12-31 23:59:59.999999999
print(y.end_time)

print(y.is_leap_year)

#Month
m = pd.Period('2017-12')
print(m)
print(m.start_time)
print(m.end_time)
#Month addition
print(m+1)

#Daily
d = pd.Period('2016-02-28', freq='D')
print(d)
print(d.start_time)
print(d.end_time)
#Daily addition
print(d+1)

#Hourly
h = pd.Period('2017-08-15 23:00:00',freq='H')
print(h)
print(h+1)
print(h+pd.offsets.Hour(1))

#Quarterly
q1= pd.Period('2017Q1', freq='Q-JAN')
print(q1)
print(q1.start_time)
print(q1.end_time)

#Change quarterly to monthly
print(q1.asfreq('M',how='start'))
print(q1.asfreq('M',how='end'))

#Weekly
w = pd.Period('2017-07-05',freq='W')
print(w)

w2 = pd.Period('2018-03-31', freq='W')

#Prints out number of weeks between these 2 week periods.
print(w2-w)

#Period Range
r = pd.period_range('2011', '2017', freq='q')
print(r)

print(r[0].start_time)
print(r[0].end_time)

#Wallmart fiscal year ends jan-31
r = pd.period_range('2011', '2017', freq='q-jan')
print(r)

print(r[0].start_time)
print(r[0].end_time)

idx = pd.PeriodIndex(start='2016-01', freq='3M', periods=10)
print(idx)

import numpy as np
#Generate random normal distribution number
ps = pd.Series(np.random.randn(len(idx)), idx)
print(ps)

#Partial index
print(ps['2016'])
print(ps['2016':'2017'])

#Converting ranges to timestamps
pst = ps.to_timestamp()
print(pst)

print(pst.index)

#Convert to period
ps = pst.to_period()
print(ps)

print(ps.index)

import pandas as pd
df = pd.read_csv("wmt.csv")

print(df)

df.set_index("Line Item",inplace=True)
#Transpose matrix
df = df.T
print(df)

#Make Fiscal Quarter ending Jan 31
df.index = pd.PeriodIndex(df.index, freq="Q-JAN")
print(df)

print(df.index)
print(df.index[0].start_time)
print(df.index[0].end_time)

df["Start Date"]=df.index.map(lambda x: x.start_time)
df["End Date"]=df.index.map(lambda x: x.end_time)
print(df)

