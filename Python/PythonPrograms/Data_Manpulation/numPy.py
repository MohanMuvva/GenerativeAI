import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# File path
file_path = 'C:\\Users\\ASUS\\gen-ai\\healthcare_dataset\\healthcare_dataset.csv'

# Load the dataset
df = pd.read_csv(file_path)

# Print basic information about the dataset
print(df.info())
print("\nFirst few rows of the dataset:")
print(df.head())

# Analyze test results
test_results = df['TestResults'].value_counts()
print("\nTestResults Distribution:")
print(test_results)

# Calculate percentages
test_results_percentage = test_results / len(df) * 100

# 1. Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(test_results, labels=test_results.index, autopct='%1.1f%%', startangle=90)
plt.title('TestResults Distribution')
plt.show()

# 2. Bar Chart
plt.figure(figsize=(10, 6))
test_results.plot(kind='bar')
plt.title('TestResults Count')
plt.xlabel('TestResult')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# 3. Histogram (for Age)
plt.figure(figsize=(10, 6))
df['Age'].hist(bins=20)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Additional analysis: Age statistics for each test result
age_stats = df.groupby('TestResults')['Age'].agg(['mean', 'median', 'min', 'max'])
print("\nAge statistics for each test result:")
print(age_stats)

# Plotting age distribution for each test result
plt.figure(figsize=(10, 6))
for result in df['TestResults'].unique():
    df[df['TestResults'] == result]['Age'].hist(alpha=0.5, label=result, bins=20)
plt.title('Age Distribution by Test Result')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.legend()
plt.tight_layout()
plt.show()

# Encode TestResults and Disease (if it's not already numeric)
df['TestResults_Encoded'] = pd.Categorical(df['TestResults']).codes

# Check if 'Disease' column exists and encode it if it does
if 'Disease' in df.columns:
    df['Disease_Encoded'] = pd.Categorical(df['Disease']).codes
else:
    print("Warning: 'Disease' column not found in the dataset.")

# Select columns for correlation
columns_for_correlation = ['Age', 'TestResults_Encoded']
if 'Disease' in df.columns:
    columns_for_correlation.append('Disease_Encoded')

# Correlation analysis
correlation_matrix = df[columns_for_correlation].corr()
print("\nCorrelation Matrix between Age, Test Results, and Disease:")
print(correlation_matrix)

# Heatmap of correlation matrix
plt.figure(figsize=(10, 8))
im = plt.imshow(correlation_matrix, cmap='coolwarm', aspect='auto')
plt.colorbar(im)
plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.title('Correlation Heatmap: Age, Test Results, and Disease')

# Add correlation values in each cell
for i in range(len(correlation_matrix.columns)):
    for j in range(len(correlation_matrix.columns)):
        text = plt.text(j, i, f"{correlation_matrix.iloc[i, j]:.2f}",
                        ha="center", va="center", color="black")

plt.tight_layout()
plt.show()

# Scatter plot matrix
fig, axes = plt.subplots(len(columns_for_correlation), len(columns_for_correlation), figsize=(12, 12))
fig.suptitle('Scatter Plot Matrix: Age, Test Results, and Disease', fontsize=16)

for i, col1 in enumerate(columns_for_correlation):
    for j, col2 in enumerate(columns_for_correlation):
        ax = axes[i, j]
        if i != j:
            ax.scatter(df[col2], df[col1], alpha=0.5)
            ax.set_title(f'Corr: {correlation_matrix.loc[col1, col2]:.2f}')
        else:
            ax.hist(df[col1], bins=20)
        if i == len(columns_for_correlation) - 1:
            ax.set_xlabel(col2)
        if j == 0:
            ax.set_ylabel(col1)
        ax.label_outer()

plt.tight_layout()
plt.show()

# If Disease column exists, create a scatter plot for Age vs Disease
if 'Disease' in df.columns:
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Age'], df['Disease_Encoded'], alpha=0.5)
    plt.title('Age vs Disease')
    plt.xlabel('Age')
    plt.ylabel('Disease (Encoded)')
    plt.tight_layout()
    plt.show()
