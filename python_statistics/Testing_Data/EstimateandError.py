import pandas as pd
import numpy as np
from scipy import stats

# Load the dataset
file_path = 'C:\\Users\\ASUS\\genai\\module_5\\healthcare_dataset\\healthcare_dataset.csv'  # Replace with your actual file path
data = pd.read_csv(file_path)

# Let's focus on 'Age' column for this example
ages = data['Age'].dropna()  # Remove any missing values

# Step 1: Point Estimate (Mean)
point_estimate = np.mean(ages)
print(f"Point Estimate (Mean Age): {point_estimate:.2f}")

# Step 2: Margin of Error
# For a 95% confidence level, the Z-score is 1.96 for a normal distribution
confidence_level = 0.95
z_score = stats.norm.ppf(1 - (1 - confidence_level) / 2)

# Calculate standard deviation and margin of error
std_dev = np.std(ages, ddof=1)  # ddof=1 for sample standard deviation
sample_size = len(ages)
standard_error = std_dev / np.sqrt(sample_size)
margin_of_error = z_score * standard_error

print(f"Margin of Error: ±{margin_of_error:.2f}")

# Confidence interval
confidence_interval = (point_estimate - margin_of_error, point_estimate + margin_of_error)
print(f"95% Confidence Interval for the Mean Age: {confidence_interval[0]:.2f} to {confidence_interval[1]:.2f}")

# Step 3: Hypothesis Test (t-test) to check if the mean is significantly different from a hypothetical value (e.g., 50 years)
hypothesized_mean = 50  # Hypothetical population mean

# Perform one-sample t-test
t_stat, p_value = stats.ttest_1samp(ages, hypothesized_mean)

print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

# Step 4: Decision based on the significance level (α)
alpha = 0.05  # Common significance level
if p_value < alpha:
    print("Reject the null hypothesis. The mean age is significantly different from 50.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference from 50.")
