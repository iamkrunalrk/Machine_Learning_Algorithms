"""
# Simple Linear Regression Model with Scikit Library
import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data
X = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([2,4,5,4,5])

# Create a linear regresion model
model = LinearRegression()

# Fit the model to the data
model.fit(X,y)

# Predict the output for a new input 
new_X = np.array([6]).reshape(-1,1)
pred_y = model.predict(new_X)

# Print the coefficient (beta_0 and beta_1)
print(f"Intercept (beta_0): {model.intercept_}")
print(f"Slope (beta_1): {model.coef_}")
print(f"Predicted y for new_X: {pred_y}")
"""

# Simple Linear Regression Model without Scikit library
# Sample data
X = [1,2,3,4,5] # Input feature
y = [2,4,5,4,5] # Output feature

# Calculate the means of X and y
mean_X = sum(X) / len(X)
mean_y = sum(y) / len(y)

# Calculate the slope (beta_0) and intercept (beta_1)
numer = sum((X[i] - mean_X) * (y[i] - mean_y) for i in range (len(X)))
denom = sum((X[i] - mean_X) ** 2 for i in range (len(X)))

beta_1 = numer / denom
beta_0 = mean_y - beta_1 * mean_X

# Predict the output for a new X
new_X = 6
predicted_y = beta_0 + beta_1 * new_X

# Print the coeefficient (beta_0 and beta_1) and the predicted y
print(f"Intercept (beta-0): {beta_0}")
print(f"Slope (beta_1): {beta_1}")
print(f"Predicted y for new X: {predicted_y}")