import numpy as np
import pandas as pd

dataset = pd.read_csv("cars.csv")
dataset.set_index("Car", inplace = True)
print (dataset)
dataset.drop("BMW", inplace = True)
print (dataset)
isinstance(dataset["Model"], int)

modelVolume = dataset["Volume"]
print (modelVolume["Audi"])


#duplicate items, phone number format standardisation, date should be same format,