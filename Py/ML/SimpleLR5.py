#import numpy library
import numpy as np

#defining the function to calculate y
def linear_regression(x, m, c):
    y = m*x + c
    return y

#defining the cost function
def cost_function(x, y, m, c):
    N = len(x)
    total_cost = 0
    
    for i in range(N):
        total_cost += (y[i] - (m*x[i] + c))**2
        
    return total_cost/N

#defining the function to update the parameters
def update_parameters(x, y, m, c, learning_rate):
    m_deriv = 0
    c_deriv = 0
    N = len(x)

    for i in range(N):
        m_deriv += -(2/N)*x[i]*(y[i]-(m*x[i]+c))
        c_deriv += -(2/N)*(y[i]-(m*x[i]+c))

