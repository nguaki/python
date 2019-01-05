import pandas as pd
df = pd.read_csv('nyc_weather.csv')
print df

#Prints out max temperature
maxTemp = df['Temperature'].max()
print "maxTemp is "
print maxTemp

#Prints out days with Rain events
print df['EST'][df['Events']=='Rain']

#First fill NaN with 0s.
#Get the mean.
df.fillna(0, inplace=True)
print df['WindSpeedMPH'].mean()

