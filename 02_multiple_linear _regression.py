# Sample data (input features and output variable)
X1 = [1, 2, 3, 4, 5, 6] # Input feaure 1
X2 = [3, 4, 5, 6, 7, 8] # Input feature 2
y = [2, 3, 4, 5, 6, 7] # Output variable

# Calculate the mean of X1, X2 and y
mean_X1 = sum(X1) / len(X1)
mean_X2 = sum(X2) / len(X2)
mean_y = sum(y) / len(y)

# Calculate the coefficient beta_0, beta_1, and beta_2
numer1 = sum((X1[i] - mean_X1) * (y[i] - mean_y) for i in range (len(X1)))
numer2 = sum((X2[i] - mean_X2) * (y[i] - mean_y) for i in range (len(X2)))

denom1 = sum((X1[i] - mean_X1) ** 2 for i in range (len(X1)))
denom2 = sum((X2[i] - mean_X2) ** 2 for i in range (len(X2)))

beta_0 = mean_y - (numer1 / denom1) * mean_X1 - (numer2 - denom2) * mean_X2
beta_1 = numer1 / denom1
beta_2 = numer2 / denom2

# Predict the output for a new input feature
new_X1 = 7
new_X2 = 9
predicted_y = beta_0 + beta_1 * new_X1 + beta_2 * new_X2

# Print the coefficients (beta_0, beta_1, beta_2) and the predicted y
print(f"Intercept (beta_0): {beta_0}")
print(f"Coefficient for X1 (beta_1): {beta_1}")
print(f"Coefficient for X2 (beta_2): {beta_2}")
print(f"Predicted Y for new X1 and X2: {predicted_y}")