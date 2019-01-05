import pandas as pd

#Converting string date to class date
df = pd.read_csv("weather_data.csv",parse_dates=['day'])
print (type(df.day[0]))
print (df)

#Set day as index.  Remove default numerical index.
df.set_index('day',inplace=True)
print (df)

#Replace NaN with 0.
new_df = df.fillna(0)
print (new_df)

#define NaN replacement per column
new_df = df.fillna({
        'temperature': 0,
        'windspeed': 0,
        'event': 'No Event'
    })
print (new_df)

#In case NaN, forward fill.  This means copy from the previous cell.
new_df = df.fillna(method="ffill")
print (new_df)


#In case NaN, backward fill.  This means copy from the above cell.
new_df = df.fillna(method="bfill")
print (new_df)

#In case NaN, backward fill from the nearest column.  
new_df = df.fillna(method="bfill", axis="columns") # axis is either "index" or "columns"
print (new_df)

#In case NaN, forward fill just one row.
new_df = df.fillna(method="ffill",limit=1)
print (new_df)

#In case NaN, fill by interpolation.
new_df = df.interpolate()
print (new_df)

#In case NaN, fill by interpolation with time.
new_df = df.interpolate(method="time") 
print (new_df)


#In case one column is NaN, drop rows with NaN
new_df = df.dropna()
print (new_df)

#In case every column isNaN, drop rows with NaN
new_df = df.dropna(how='all')
print (new_df)

#Not sure what this does but gives same results as above.
new_df = df.dropna(thresh=1)
print (new_df)

#creates new range of dates.
dt = pd.date_range("01-01-2017","01-11-2017")
idx = pd.DatetimeIndex(dt)
print (df.reindex(idx))