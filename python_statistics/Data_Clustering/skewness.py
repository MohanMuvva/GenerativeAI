import numpy as np
from scipy.stats import skew

# Create the dataset
data = np.arange(0, 11)  # This creates an array [1, 2, 3, ..., 10]

# Calculate mean
mean = np.mean(data)
# Calculate median
median = np.median(data)
# Calculate variance
variance = np.var(data, ddof=0)  # Population variance
# Calculate standard deviation
std_deviation = np.std(data, ddof=0)  # Population standard deviation
# Calculate skewness
skewness = skew(data)

# Print the results
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_deviation}")
print(f"Skewness: {skewness}")
