#import subtract as sub
from subtract import subtract
from format_report import format_report

import pandas as pd


i = 0

def a():
    global i
    print('A')
    i = i + 1
    print(i)
    
def b():
    global i
    print('B')
    i = i + 1
    print(i)
    
def c(): 
    global i
    print('C')
    i = i + 1
    print(i)
    
    
a()
b()
c()

#ans = sub.subtract(5,2)
ans = subtract(5,2)

df = pd.DataFrame()
df['col1'] = [1,2,3]
df['col2'] = [2,3,4]

print(ans)

format_report(df)