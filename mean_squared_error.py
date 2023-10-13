import numpy as np

# Actual value (ground truth)
actual_values = np.array([2, 4, 5, 4, 5])

# Predicted value from your model
predicted_value = np.array([2.2, 3.8, 5.1, 4.2, 4.9])

# Calculate MSE
mse = np.mean((predicted_value - actual_values) ** 2 )

print(f"Mean Squared Error: {mse}")