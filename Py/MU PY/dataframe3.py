import numpy as np
import pandas as pd

df = pd.DataFrame({
    "Name" : ['a', 'b', 'c', 'd'],
    "Marks" : [5, np.nan, np.nan, 7]
})
print (df)
meanVal = df.Marks.mean()
print (meanVal)
df.set_index("Name", inplace= True)
print (df)
print ('')

df1 = pd.DataFrame({"a": [1, 2, 3, 4], "b": [5, 6, 7, 8]})

df2 = pd.DataFrame({"a": [1, 2, 3], "b" : [4, 5, 6]})

df3 = df1.append(df2, ignore_index= True)
print (df3)

df3.drop([df3.index[2], df3.index[3]], inplace = True)
print (df3)
na = df.isna().sum()
print (na)