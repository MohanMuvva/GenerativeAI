import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'C:\\Users\\ASUS\\Downloads\\Industrial_Policy_Dataset.csv'  # Update with your actual file path
df = pd.read_csv(file_path)

# Check the first few rows to understand the structure
print(df.head())

# Check for null values in the industry column
industry_col = 'Industry'  # Replace with the actual column name for industries
print("\nChecking for null values in the industry column:")
print(df[industry_col].isnull().sum())

# Clean the industry column if necessary (e.g., removing leading/trailing spaces)
df[industry_col] = df[industry_col].str.strip()

# Group data by industry and calculate mean investment and production output
industry_analysis = df.groupby(industry_col).agg({
    'Investment (in Million INR)': 'mean',  # Replace with actual column name
    'Production Output (in Million INR)': 'mean'  # Replace with actual column name
}).reset_index()

print("\nIndustry Analysis (Mean Investment and Production Output):")
print(industry_analysis)

# Visualize the average investment by industry
plt.figure(figsize=(12, 6))
sns.barplot(x=industry_col, y='Investment (in Million INR)', data=industry_analysis)
plt.title('Average Investment by Industry')
plt.xticks(rotation=45)
plt.ylabel('Average Investment (in Million INR)')
plt.show()

# Visualize the average production output by industry
plt.figure(figsize=(12, 6))
sns.barplot(x=industry_col, y='Production Output (in Million INR)', data=industry_analysis)
plt.title('Average Production Output by Industry')
plt.xticks(rotation=45)
plt.ylabel('Average Production Output (in Million INR)')
plt.show()

# Optional: Box plot to visualize the distribution of production output by industry
plt.figure(figsize=(12, 6))
sns.boxplot(x=industry_col, y='Production Output (in Million INR)', data=df)
plt.title('Distribution of Production Output by Industry')
plt.xticks(rotation=45)
plt.ylabel('Production Output (in Million INR)')
plt.show()
