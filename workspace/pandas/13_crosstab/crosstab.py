import pandas as pd
df = pd.read_excel("survey.xls")
print(df)

#Moves nationality to row and Handedness was smart enough to split into left and
#right with columns
print(pd.crosstab(df.Nationality,df.Handedness))

#Moves Sex to row and Handedness was smart enough to split into left and
#right with columns
print(pd.crosstab(df.Sex,df.Handedness))

#margins tells to include sum.
print(pd.crosstab(df.Sex,df.Handedness, margins=True))

#Brings sex to identify rows and has 2 levels of columns.
#Top header is Handedness and lower header is nationality.
print(pd.crosstab(df.Sex, [df.Handedness,df.Nationality], margins=True))

#Brings 2 levels of row identification.
#Outer level is Nationality and inner level is sex.
print(pd.crosstab([df.Nationality, df.Sex], [df.Handedness], margins=True))

#Normalize data
#Can easily read percentage.
print("----------")
print(pd.crosstab(df.Sex, df.Handedness, normalize='index'))

import numpy as np
#Calculate average age by left or right
print(pd.crosstab(df.Sex, df.Handedness, values=df.Age, aggfunc=np.average))
