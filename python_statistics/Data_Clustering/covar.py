import pandas as pd

# Load the dataset
file_path = 'C:\\Users\\ASUS\\genai\\module_5\\healthcare_dataset\\healthcare_dataset.csv'
df = pd.read_csv(file_path)

# Display the first few rows of the dataset to understand its structure
print(df.head())

# Assuming the dataset has numerical columns like 'Age', 'TestResults', and 'BloodPressure'
# Let's calculate covariance and correlation between 'Age' and 'TestResults'
# First, ensure that 'TestResults' is numeric (if it's categorical, we may need to encode it)

# Example: Convert 'TestResults' to numeric if it's categorical
df['TestResults'] = df['TestResults'].map({'Positive': 1, 'Negative': 0})

# Calculate Covariance
covariance = df[['Age', 'TestResults']].cov().iloc[0, 1]
print(f"Covariance between Age and Test Results: {covariance:.4f}")

# Calculate Correlation
correlation = df[['Age', 'TestResults']].corr().iloc[0, 1]
print(f"Correlation between Age and Test Results: {correlation:.4f}")

# Interpretation of Covariance and Correlation
if covariance > 0:
    print("Covariance indicates a positive relationship between Age and Test Results.")
elif covariance < 0:
    print("Covariance indicates a negative relationship between Age and Test Results.")
else:
    print("Covariance indicates no relationship between Age and Test Results.")

if correlation > 0.5:
    print("There is a strong positive correlation between Age and Test Results.")
elif correlation < -0.5:
    print("There is a strong negative correlation between Age and Test Results.")
elif 0 < correlation <= 0.5:
    print("There is a moderate positive correlation between Age and Test Results.")
elif -0.5 < correlation < 0:
    print("There is a moderate negative correlation between Age and Test Results.")
else:
    print("There is no correlation between Age and Test Results.")

# Causation Discussion
print("\nCausation Interpretation:")
print("While covariance and correlation can indicate relationships between variables, they do not imply causation.")
print("To establish causation, further analysis such as controlled experiments or longitudinal studies is required.")
print("For example, even if older age correlates with positive test results, it does not mean that age causes the test results.")
