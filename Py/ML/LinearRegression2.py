import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("tvmarketing.csv")
print (df)

# w and b values

def linear_regression(X, y, m_current=0, b_current=0, epochs=1000, learning_rate=0.0001):
     N = float(len(y))
     for i in range(epochs):
          y_current = (m_current * X) + b_current
          m_gradient = -(2/N) * sum(X * (y - y_current))
          b_gradient = -(2/N) * sum(y - y_current)
          m_current = m_current - (learning_rate * m_gradient)
          b_current = b_current - (learning_rate * b_gradient)
     return m_current, b_current

print (linear_regression(df["TV"], df["Sales"], m_current=0, b_current=0, epochs=10000, learning_rate=0.00001))