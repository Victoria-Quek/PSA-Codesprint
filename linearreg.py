import numpy as np
from sklearn.linear_model import LinearRegression

# input data
# we need to provide some data to determine what is the ideal weights

def data():
    return

# Linear Regression
X = np.array([[1, 1],
              [1, 2],
              [2, 2],
              [2, 3]]) # values of input variables
y = np.dot(X, np.array([1, 2])) + 3 # expected output
print(X)
print(y)
reg = LinearRegression().fit(X, y)
print("R^2 value:", reg.score(X, y)) # R^2 value
print("Coefficients:", reg.coef_) # b1, b2, ...
print("Intercept:", reg.intercept_) # b0
