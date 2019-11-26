import pandas as pd

india_weather = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
    "humidity": [80, 60, 78]
})

print (india_weather)

us_weather = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
    "humidity": [68, 65, 75]
})
print (us_weather)

#Concatenates both weathers.
df = pd.concat([india_weather, us_weather])
print (df)

print('----------------')
#Fixes index problem.       
df = pd.concat([india_weather, us_weather], ignore_index=True)
print (df)
print('----------------')

#Groups rows with labels.
df = pd.concat([india_weather, us_weather], keys=["india", "us"])
print (df)

#Just print the US cities
print(df.loc["us"])

#Just print the INDIA cities
print(df.loc["india"])


temperature_df = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
}, index=[0,1,2])
print(temperature_df)

windspeed_df = pd.DataFrame({
    "city": ["delhi","mumbai"],
    "windspeed": [7,12],
}, index=[1,0])
print(windspeed_df)

#concatenation with equal index.
df = pd.concat([temperature_df,windspeed_df],axis=1)
print(df)

#Creating a series
s = pd.Series(["Humid","Dry","Rain"], name="event")
print(s)

#Concatenation DF with a series
df = pd.concat([temperature_df,s],axis=1)
print(df)
