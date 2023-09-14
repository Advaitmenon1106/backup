import numpy as np
import pandas as pd

dataset = pd.read_csv("data1.csv")
print (dataset)
print (dataset['Pulse'])
print (dataset.describe())
print ("")
print (dataset[dataset['Duration']>60])
print ("")
print (dataset.Duration)
print ("")
print (dataset.Duration == 60)
print ("")
