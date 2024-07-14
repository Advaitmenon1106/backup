import numpy as np
import pandas as pd
import sklearn as sk

horror = np.array(["horror", "Thrillers", "Thriller", "Mystery", "mystery"])

while (True):
    file = input("Enter a file directory: ")
    f = open(file)
    lines = f.readlines()
    print (lines)