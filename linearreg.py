import numpy as np
from sklearn.linear_model import LinearRegression
import inquirer

# input data
# we need to provide some data to determine what is the ideal weights
def query():
    start = input("Enter your current location: ")
    end = input("Enter your destination: ")
    print(answers["size"])

query()

# how to let them select options
# questions = [inquirer.List('size',
#                           message="What size do you need?",
#                           choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
#                           ),
#             ]
# answers = inquirer.prompt(questions)

# Linear Regression

# travel time: feature scaling (scale from 0 to 1)
# distance: feature scaling (scale from 0 to 1)

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
