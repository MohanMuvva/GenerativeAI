import numpy as np

# Original data
data = np.array([150, 160, 170, 180, 190, 200, 210, 220, 230, 240])

# Calculate mean and standard deviation
mean = np.mean(data)
std_dev = np.std(data)

# Standardize data
standardized_data = (data - mean) / std_dev

# Calculate mean and standard deviation of standardized data to verify
standardized_mean = np.mean(standardized_data)
standardized_std_dev = np.std(standardized_data)

print('mean, std_dev, standardized_data, standardized_mean, standardized_std_dev')

print(f"\nmean: {mean}, standardized_data: {standardized_data}")

