import pandas as pd
df = pd.read_csv("aapl_no_dates.csv")
print(df.head())

#Note that July 4th is picked up as a business holiday.
rng = pd.date_range(start="7/1/2017", end="7/21/2017", freq='B')
print(rng)

#Now do not include holiday as business day.
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

us_cal = CustomBusinessDay(calendar=USFederalHolidayCalendar())

rng = pd.date_range(start="7/1/2017",end="7/23/2017", freq=us_cal)
print(rng)

df.set_index(rng,inplace=True)
print(df.head())


#Customized holidays.  Good case for this is birthday.
from pandas.tseries.holiday import AbstractHolidayCalendar, nearest_workday, Holiday
class myCalendar(AbstractHolidayCalendar):
    rules = [
        Holiday('My Birth Day', month=4, day=15),#, observance=nearest_workday),
    ]
    
my_bday = CustomBusinessDay(calendar=myCalendar())
print(pd.date_range('4/1/2017','4/30/2017',freq=my_bday))

#Egypt business days are Sun~Thu
egypt_weekdays = "Sun Mon Tue Wed Thu"

b = CustomBusinessDay(weekmask=egypt_weekdays)

print(pd.date_range(start="7/1/2017",periods=20,freq=b))

#Include both customized holidays and weekmask for business days
b = CustomBusinessDay(holidays=['2017-07-04', '2017-07-10'], weekmask=egypt_weekdays)

print(pd.date_range(start="7/1/2017",periods=20,freq=b))

from datetime import datetime
dt = datetime(2017,7,9)
print(dt)

#add 1 business day
print(dt + 1*b)