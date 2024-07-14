import numpy as np
import pandas as pd

no_nodes = int(input("How many nodes?"))
nodes = np.empty(shape=no_nodes, dtype=str)

# Entering nodes
for i in range(0, len(nodes)):
    n = input('Enter a node: ')
    nodes[i] = n

adjDf = pd.DataFrame(index=nodes, columns=nodes)

for i in nodes:
    for j in nodes:
        element = input("Connect {} and {} ?".format(i, j))
        if element == 'Y' or element == 'y' or element == 'Yes' or element == 'yes':
            adjDf.loc[i, j] = 1
        else:
            adjDf.loc[i, j] = 0

print(adjDf)
