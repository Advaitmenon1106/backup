import numpy as np
import pandas as pd

dataset = pd.read_csv("data (1).csv")

na = dataset.isna().sum()
print (na)
meanVal = dataset.mean()
dataset.fillna(meanVal)
na2 = dataset.isna().sum
print (na2)
