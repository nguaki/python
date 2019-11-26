import pandas as pd

l1 = []
l2 = []
l3 = []

for i in range(0,9):
    l1.append(i)
    l2.append(i+1)
    l3.append(i+2)
    
df1 = pd.DataFrame()
df1['col1'] = l1
df1['col2'] = l2
df1['col3'] = l3

print(df1)

df2 = pd.DataFrame( { 'colA': l1, 'colB': l2, 'colC': l3})
print(df2)

import numpy as np

df3 = pd.DataFrame( np.column_stack([l1, l2, l3]), columns=['A', 'B', 'C'])
print(df3)