import pandas as pd
df = pd.read_csv("fb.csv",parse_dates=['Date'],index_col='Date')
print(df)

print(df.shift(1))
print(df.shift(-1))

df['Prev Day Price'] = df['Price'].shift(1)
print(df)

df['Price Change'] = df['Price'] - df['Prev Day Price']
print(df)

df['5 day return'] =  (df['Price'] - df['Price'].shift(5))*100/df['Price'].shift(5)
print(df)