import pandas as pd

df = pd.read_excel('stocks.xlsx', sheetname='stock_price', header=[0, 1] )
print (pd.__version__)

#df = pd.read_excel('stocks.xlsx', sheetname='stock_price', header=1)

print(df)

#Reshape the matrix with stack() call
print (df.stack())

#Move header 0 to row
print (df.stack(level=0))

#when level is not identified, it is the highest level header which is 
#moving to row identifier.
df_stacked=df.stack()
print (df_stacked)

#Moving row identifier to column identifier
df_stacked.unstack()

#Reade 3 levels of headers
df2 = pd.read_excel("stocks_3_levels.xlsx",header=[0,1,2])
print(df2)

#Bring the header level 2 to identify rows.
print (df2.stack())

#Bring the header level 0 to identify rows.
print (df2.stack(level=0))

print(df2.stack(level=1))
print(df2.stack(level=2))