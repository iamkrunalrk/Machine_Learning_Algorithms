import numpy as np

# Define the sigmoid (logistic function)
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Sample data
X = np.array([[1.2], [2.4], [3.1], [4.5], [5.0]])

# Model parameters (coefficient)
theta = np.array([1.0])

# Calculate the linear combination of features and parameters
z = np.dot(X, theta)

# Predict the probability of belonging to the positive class
predicted_probability = sigmoid(z)

print("Predicted Probabilities:")
for i, prob in enumerate(predicted_probability):
    print(f"Inout {i+1}: Probability of class 1: {prob: .4f}")