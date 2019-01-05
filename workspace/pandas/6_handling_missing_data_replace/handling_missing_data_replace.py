import pandas as pd
import numpy as np
df = pd.read_csv("weather_data.csv")

print (df)

#Replaces -99999 with NaN
new_df = df.replace(-99999, value=np.NaN)
print (new_df)

#Replaces -99999, -88888 with NaN
new_df = df.replace(to_replace=[-99999,-88888], value=0)
print (new_df)

#replace by column
#For temperature column, replace -99999 with NaN.
#For windspeed column, replace -99999 with NaN.
#For event column, replace 0 with NaN
new_df = df.replace({
        'temperature': -99999,
        'windspeed': -99999,
        'event': '0'
    }, np.nan)
print (new_df)

#replace by mapping
new_df = df.replace({
        -99999: np.nan,
        'no event': 'Sunny',
    })
print (new_df)

#Regex replacement
#Removes all characters.
# when windspeed is 6 mph, 7 mph etc. & temperature is 32 F, 28 F etc.
new_df = df.replace({'temperature': '[A-Za-z]', 'windspeed': '[a-z]'},'', regex=True) 
print (new_df)

#Creating DF directly.
df = pd.DataFrame({
    'score': ['exceptional','average', 'good', 'poor', 'average', 'exceptional'],
    'student': ['rob', 'maya', 'parthiv', 'tom', 'julian', 'erica']
})
print (df)

#Mapping a list to another list.
df = df.replace(['poor', 'average', 'good', 'exceptional'], [1,2,3,4])
print (df)

