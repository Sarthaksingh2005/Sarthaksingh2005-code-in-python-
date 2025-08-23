import pandas as pd
##pandas data structure
##1D
data=[10,20,30,40]
s=pd.Series(data)
print(s)

import pandas as pd

data = {
    "Name": ["Sarthak", "Aman", "Riya"],
    "Age": [21, 22, 20],
    "Marks": [90, 85, 88]
}
#read data#
df = pd.DataFrame(data)
print(df)

#explore data#
df.shape      # (rows, columns)
df.info()     # column info
df.describe() # summary stats (mean, std, etc.)

#indexing and selection
print(df["Name"])       # select column
print(df.iloc[0])       # first row
print(df.loc[1, "Marks"]) # row 1, column 'Marks'

#filtering
print(df[df["Marks"] > 85])  # students with marks > 85

