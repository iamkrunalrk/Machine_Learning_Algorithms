import numpy as np

# Sample data (input features and output variables)
X = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])

# Specify the degree of the polynomial
degree = 2

# Create a matrix of polynomial features
X_poly = np.column_stack([X**i for i in range(1, degree + 1)])

# Add a column of 1 for the intercept term
X_poly = np.column_stack([np.ones_like(X_poly[:, 0]), X_poly])

# Calculate the coefficient beta_0, beta_1, beta_2, ...
coefficient = np.linalg.inv(X_poly.T @ X_poly) @ X_poly.T @ y

# Predict the output for a new input
new_X = 6
new_poly_X = np.array([1] + [new_X ** i for i in range (1, degree + 1)])

predicted_y = new_poly_X @ coefficient

# print the coefficient and new predicted y
print(f"Coefficient: {coefficient}")
print(f"Predicted y for new X: {predicted_y}")