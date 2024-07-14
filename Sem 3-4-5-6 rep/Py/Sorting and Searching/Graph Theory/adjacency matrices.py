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
            weight = int(input('Enter a weight: '))
            adjDf.loc[i, j] = weight
        else:
            adjDf.loc[i, j] = 0

print(adjDf)

#djikstra's greedy algorithm :-

path = ''
distance = 0

start = input('Enter a starting node: ')
end = input ('Ending node: ')
path+=start

for i in nodes:
    for j in nodes:
        if j == end:
            path+=end
            break
        else:
            next = adjDf.loc[i][adjDf.iloc[i]!=0].idxmin()
            path+=next
            distance+=adjDf.loc[i][adjDf.iloc[i]!=0].min()