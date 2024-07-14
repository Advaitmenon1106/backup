import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Book1.csv")
print (df)

# w and b values
w = 0
b = 0
LR = 0.0001
it = 10000

X = np.array(df["X"])
X = X/max(X)
#X = (X-df["X"].mean())/max(X)
Y = np.array(df["Y"])
Yn = Y/max(Y)

for x in range(it):
    Yhat = (w*X) + b
    DiffWRTw = (1/float(len(X)))*((X*(Yhat-Y)).sum())
    DiffWRTb = (1/float(len(X)))*((Yhat-Y).sum())
    w = w-(LR*DiffWRTw)
    b = b-(LR*DiffWRTb)

print (w, b)

plt.scatter(X, Y)
plt.plot([min(X), max(X)], [min(Yhat), max(Yhat)], color="red")
plt.show()