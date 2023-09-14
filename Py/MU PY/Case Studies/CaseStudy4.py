import numpy as np
import pandas as pd

df = pd.read_csv("MU Case Study 2.csv")
print (df)
priorProb = {"M/Elect", "M/Rock", "M/"}
df1 = df.set_index("Favorite Color")
print (df1)