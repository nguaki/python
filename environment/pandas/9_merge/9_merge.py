import pandas as pd
df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
})
print(df1)

df2 = pd.DataFrame({
    "city": ["chicago","new york","orlando"],
    "humidity": [65,68,75],
})
print(df2)

#default is inner join
df3 = pd.merge(df1, df2, on="city")
print("Merge on city")
print(df3)

df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35, 38],
})
print(df1)

df2 = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "humidity": [65,68,71],
})
print(df2)

df3=pd.merge(df1,df2,on="city",how="inner")
print("Inner Merge on city")
print(df3)

df3=pd.merge(df1,df2,on="city",how="outer")
print("Outer Merge on city")
print(df3)

df3=pd.merge(df1,df2,on="city",how="left")
print("Left Merge on city")
print(df3)

df3=pd.merge(df1,df2,on="city",how="right")
print("Right Merge on city")
print(df3)

#interpreted error on indicator
#df3=pd.merge(df1,df2,on="city",how="outer",indicator=True)

df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35,38],
    "humidity": [65,68,71, 75]
})

print (df1)

df2 = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "temperature": [21,14,35],
    "humidity": [65,68,71]
})
print (df2)

df3= pd.merge(df1,df2,on="city",how="outer", suffixes=('_first','_second'))
print("suffixes Outer Merge on city")
print (df3)

df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
})
#Removes index column
df1.set_index('city',inplace=True)
print (df1)

df2 = pd.DataFrame({
    "city": ["chicago","new york","orlando"],
    "humidity": [65,68,75],
})
df2.set_index('city',inplace=True)
print (df2)

df1 = df1.join(df2,lsuffix='_l', rsuffix='_r')
print("rsuffixes inner Merge on city")
print (df1)