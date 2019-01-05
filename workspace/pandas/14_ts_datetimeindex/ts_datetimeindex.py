import pandas as pd

#Convert string date into date object
#Make Date as 1st col which makes it row identifier.
df = pd.read_csv("aapl.csv",parse_dates=["Date"], index_col="Date")

#Print first 2 rows only
print(df.head(2))

#Print out all indices
print(df.index)

#Print out single date
print(df['2017-06-30'])

#Print out group 
print(df['2017-06'])

#Print out head items
print(df['2017-06'].head())

#Average price for June of 2017
print(df['2017-06'].Close.mean())

#Retrieve head 2 rows of 2017
print(df['2017'].head(2))

#Retrieve range of dates
print(df['2017-01-08':'2017-01-03'])

#Get one row of month end mean 
print(df['Close'].resample('M').mean().head())