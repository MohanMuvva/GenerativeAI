import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
file_path = 'C:\\Users\\ASUS\\Downloads\\filtered_data_month_1.csv'
filtered_df = pd.read_csv(file_path)

# Check the dataset structure
print(filtered_df.head())
print(filtered_df.columns)

# Check for missing values
missing_values = filtered_df.isnull().sum()
print("Missing values in each column:")
print(missing_values)

# Check for duplicate rows
duplicate_rows = filtered_df.duplicated().sum()
print(f"Number of duplicate rows: {duplicate_rows}")

# Basic statistics of the dataset
basic_stats = filtered_df.describe()
print("Basic statistics of the dataset:")
print(basic_stats)

# Convert columns to appropriate types (categorical for specific fields)
filtered_df['rate_code'] = filtered_df['rate_code'].astype('category')
filtered_df['payment_type'] = filtered_df['payment_type'].astype('category')
filtered_df['hour_of_day'] = filtered_df['hour_of_day'].astype('category')

# Display dataset information after conversions
print(filtered_df.info())

# Histogram plots for specified variables
numeric_cols = ['trip_distance', 'fare_amount', 'tip_amount', 'tolls_amount', 'trip_duration']

plt.figure(figsize=(16, 10))
for i, col in enumerate(numeric_cols, 1):
    plt.subplot(3, 2, i)
    sns.histplot(filtered_df[col], bins=30, kde=True, color='blue', alpha=0.6)
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Prepare the data for linear regression
X = filtered_df[['trip_distance', 'fare_amount', 'tip_amount', 'tolls_amount', 'trip_duration']]  # Independent variables
y = filtered_df['total_amount']  # Dependent variable

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

# Plotting Actual vs Predicted Total Amount
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')  # 45-degree line
plt.title('Actual vs Predicted Total Amount')
plt.xlabel('Actual Total Amount')
plt.ylabel('Predicted Total Amount')
plt.grid()
plt.show()

# Visualizing the relationships between features and total_amount (example)
numeric_cols = ['trip_distance', 'fare_amount', 'tip_amount', 'tolls_amount', 'trip_duration']

plt.figure(figsize=(16, 10))
for i, col in enumerate(numeric_cols, 1):
    plt.subplot(3, 2, i)
    sns.scatterplot(x=filtered_df[col], y=filtered_df['total_amount'], alpha=0.5)
    plt.title(f'Total Amount vs {col}')
    plt.xlabel(col)
    plt.ylabel('Total Amount')

plt.tight_layout()
plt.show()

# Visualizing categorical variables and total_amount (example)
categorical_cols = ['rate_code', 'payment_type', 'hour_of_day']

plt.figure(figsize=(16, 10))
for i, col in enumerate(categorical_cols, 1):
    plt.subplot(3, 2, i)
    sns.barplot(x=filtered_df[col], y=filtered_df['total_amount'], estimator=lambda x: x.mean())
    plt.xticks(rotation=45, ha='right')
    plt.title(f'Total Amount vs {col}')
    plt.xlabel(col)
    plt.ylabel('Average Total Amount')

plt.tight_layout()
plt.show()

# Correlation Heatmap
plt.figure(figsize=(12, 8))
correlation_matrix = filtered_df[numeric_cols + ['total_amount']].corr()  # Include total_amount for correlation
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', square=True)
plt.title('Correlation Heatmap')
plt.show()
