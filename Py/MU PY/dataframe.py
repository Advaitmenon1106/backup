import numpy as np
import pandas as pd

array = [12, 3, 4, 5]

df = pd.DataFrame(array)
print (df)
print ("")
array2 = [[12, 13, 14, 15], [16, 17, 18, 19]]
df2 = pd.DataFrame(array2)
print (df2)
print ("")
df3 = pd.DataFrame(array2, columns=['a', 'b', 'c', 'd'])
print (df3)
dataset = pd.read_csv("data1.csv")
print (dataset)
sum = dataset.isna().sum()
print (sum)