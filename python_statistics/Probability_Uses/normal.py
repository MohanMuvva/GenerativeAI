import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Parameters for the normal distribution
mean = 50
std_dev = 5
num_samples = 1000

# Generate random samples from a normal distribution
data = np.random.normal(mean, std_dev, num_samples)

# Calculate the mean and standard deviation of the generated data
calculated_mean = np.mean(data)
calculated_std_dev = np.std(data)

# Print the calculated mean and standard deviation
print(f"Calculated Mean: {calculated_mean:.2f}")
print(f"Calculated Standard Deviation: {calculated_std_dev:.2f}")

# Plotting the normal distribution
plt.figure(figsize=(10, 6))
sns.histplot(data, bins=30, kde=True, stat="density", color='blue', alpha=0.6)
plt.title('Normal Distribution (Mean = 50, Std Dev = 5)')
plt.xlabel('Value')
plt.ylabel('Density')

# Overlay the theoretical normal distribution curve
x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)
plt.plot(x, y, color='red', label='Theoretical Normal Distribution', linewidth=2)

plt.legend()
plt.grid()
plt.show()

