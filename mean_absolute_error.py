import numpy as np

# Actual values (ground truth)
actual_values = np.array([2, 4, 5, 4, 5])

# Predicted values from model
predicted_values = np.array([2.2, 3.8, 5.1, 4.2, 4.9])

# Calculate the MAE
mae = np.mean(np.abs(predicted_values - actual_values))

print(f"Mean Absolute Error: {mae}")