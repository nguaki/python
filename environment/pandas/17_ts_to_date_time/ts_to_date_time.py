import pandas as pd

#converts string date to Object date.
dates = ['2017-01-05', 'Jan 5, 2017', '01/05/2017', '2017.01.05', '2017/01/05','20170105']
print(pd.to_datetime(dates))

#converts string date to Object date which includes the time.
dt = ['2017-01-05 2:30:00 PM', 'Jan 5, 2017 14:30:00', '01/05/2016', '2017.01.05', '2017/01/05','20170105']
print(pd.to_datetime(dt))

#Dealing with European style date
#This case, 30 is obviously cannot be month so it will treat 
#30 as day.
#This will convert to yyyy-mm-dd
print(pd.to_datetime('30-12-2016'))

#Acknowledge that the first numerical number is day
#prints out 2016-01-05
print(pd.to_datetime('5-1-2016', dayfirst=True))

#Custom date formate
#Uses $ as delimeter
print(pd.to_datetime('2017$01$05', format='%Y$%m$%d'))

#Uses # as delimeter
print(pd.to_datetime('2017#01#05', format='%Y#%m#%d'))

#Handling errors
#Since errors flag is ignore, this will print 'abc'
print(pd.to_datetime(['2017-01-05', 'Jan 6, 2017', 'abc'], errors='ignore'))

#Since errors flag is coerce, this will not print 'abc' but NaT(Not a time)
print(pd.to_datetime(['2017-01-05', 'Jan 6, 2017', 'abc'], errors='coerce'))

#Epoch
#Epoch or Unix time means number of seconds that have passed since Jan 1, 1970 00:00:00 UTC time
current_epoch = 1501324478
print(pd.to_datetime(current_epoch, unit='s'))
print(pd.to_datetime(current_epoch*1000, unit='ms'))

#print out an array of time
t = pd.to_datetime([current_epoch, current_epoch + 100], unit='s')
print(t)

#Get an epoch time
print(t.view('int64'))