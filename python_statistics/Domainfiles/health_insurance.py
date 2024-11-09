import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

# Load the dataset
file_path = 'C:\\Users\\ASUS\\Downloads\\insurance.csv'  # Adjust the file path as needed
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("Dataset Head:")
print(df.head())

# Data Description: Summary statistics for numerical columns
print("\nSummary statistics for numerical columns:")
print(df.describe())

# Identify numerical and categorical columns
numerical_cols = df.select_dtypes(include=np.number).columns.tolist()
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

# Display unique values for categorical columns
print("\nUnique values for categorical columns:")
for col in categorical_cols:
    print(f"{col}: {df[col].unique()}")

# Remove the dependent variable 'expenses' from numerical columns
numerical_cols.remove('expenses')

# Check for null values
print("\nNull Values in Each Column:")
print(df.isnull().sum())

# Data Cleaning: Handle missing values (if any)
df.dropna(inplace=True)

# Function to identify outliers using Interquartile Range (IQR) method
def identify_outliers_iqr(data, column_name):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Ensure that lower bounds for 'expenses', 'age', and 'children' are not negative
    if column_name in ['expenses', 'age', 'children']:
        lower_bound = max(0, lower_bound)

    return data[(data < lower_bound) | (data > upper_bound)], lower_bound, upper_bound

# Identify and handle outliers
df['is_outlier'] = False  # Add a column to mark outliers
outliers_dict = {}

for col in numerical_cols + ['expenses']:
    outliers, lower_bound, upper_bound = identify_outliers_iqr(df[col], col)
    outliers_dict[col] = outliers
    df.loc[outliers.index, 'is_outlier'] = True
    print(f"\nOutliers in '{col}' (using IQR method):")
    print(outliers)
    print(f"Lower bound: {lower_bound}, Upper bound: {upper_bound}")

# Remove the 'is_outlier' column after cleaning
df_cleaned = df.copy()  # Keep all data including outliers

print("\nDataset after cleaning (including outliers):")
print(df_cleaned.head())

# Use LabelEncoder to convert categorical variables to numerical
label_encoder = LabelEncoder()

for col in categorical_cols:
    df_cleaned[col] = label_encoder.fit_transform(df_cleaned[col])

# Create a heatmap of the correlation matrix
plt.figure(figsize=(12, 8))
correlation_matrix = df_cleaned.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', square=True)
plt.title('Correlation Heatmap')
plt.show()

# Create scatter plots and boxplots for each variable vs 'expenses'
for col in numerical_cols + categorical_cols:
    plt.figure(figsize=(8, 6))
    
    # If column is categorical, use boxplot (e.g., smoker, region)
    if col in categorical_cols:
        sns.boxplot(x=col, y='expenses', data=df_cleaned, hue='smoker', palette={1: 'red', 0: 'blue'})
        plt.title(f'Boxplot of {col} vs Expenses (Smoker vs Non-Smoker)')
        plt.legend(title='Smoker', labels=['Non-Smoker', 'Smoker'])
        
    # If column is numerical, use scatter plot (e.g., age, bmi)
    else:
        sns.scatterplot(data=df_cleaned, x=col, y='expenses', hue='smoker', palette={1: 'red', 0: 'blue'}, alpha=0.6)
        plt.title(f'Scatter plot of {col} vs Expenses')
        plt.xlabel(col)
        plt.ylabel('Expenses')

    plt.tight_layout()
    plt.show()

# Prepare data for linear regression
X = df_cleaned.drop(columns=['expenses'])  # Features
y = df_cleaned['expenses']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")

# Plotting the results
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')  # 45-degree line
plt.title('Actual vs Predicted Expenses')
plt.xlabel('Actual Expenses')
plt.ylabel('Predicted Expenses')
plt.grid()
plt.show()
