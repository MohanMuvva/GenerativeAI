import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score
import seaborn as sns
from scipy import stats

# Load the dataset
data = pd.read_csv("C:\\Users\\ASUS\\Downloads\\Healthcare-Diabetes.csv")  # Change the path as needed

# Data Cleaning: Remove rows with null values
data_cleaned = data.dropna()

# Remove rows where SkinThickness is equal to 0
data_cleaned = data_cleaned[data_cleaned['SkinThickness'] != 0]

# Check if any columns of interest have null values after cleaning
if data_cleaned.isnull().sum().any():
    print("Warning: There are still null values in the dataset after cleaning.")
else:
    print("Data cleaning complete. No null values found.")

# Check if any rows were removed due to SkinThickness being 0
if len(data) != len(data_cleaned):
    print(f"Removed {len(data) - len(data_cleaned)} rows where SkinThickness was 0.")

# Preview the dataset
print(data_cleaned.head())

# Plotting the heatmap for correlation
plt.figure(figsize=(12, 8))
correlation_matrix = data_cleaned.corr()  # Calculate the correlation matrix
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar=True)
plt.title('Correlation Heatmap')
plt.show()

# Split the dataset into features (X) and target (y)
X = data_cleaned[['Age', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction']]
y_classification = data_cleaned['Outcome']
y_regression = data_cleaned['Insulin']

# Split the data into training and test sets for classification
X_train_classification, X_test_classification, y_train_classification, y_test_classification = train_test_split(X, y_classification, test_size=0.2, random_state=42)

# Split the data into training and test sets for regression
X_train_regression, X_test_regression, y_train_regression, y_test_regression = train_test_split(X, y_regression, test_size=0.2, random_state=42)

# Logistic Regression (for classification)
logistic_model = LogisticRegression(max_iter=200)
logistic_model.fit(X_train_classification, y_train_classification)

# Predictions for classification
y_pred_classification = logistic_model.predict(X_test_classification)
accuracy = accuracy_score(y_test_classification, y_pred_classification)

# Print Logistic Regression accuracy
print(f"Logistic Regression Accuracy: {accuracy}")

# Linear Regression (for continuous value prediction)
linear_model = LinearRegression()
linear_model.fit(X_train_regression, y_train_regression)

# Predictions for regression
y_pred_regression = linear_model.predict(X_test_regression)

# Evaluate Linear Regression
r2 = r2_score(y_test_regression, y_pred_regression)
mse = mean_squared_error(y_test_regression, y_pred_regression)

# Print Linear Regression evaluation metrics
print(f"Linear Regression R^2 Score: {r2}")
print(f"Linear Regression Mean Squared Error: {mse}")

# Calculate the margin of error for the linear regression predictions
# Calculate residuals
residuals = y_test_regression - y_pred_regression

# Calculate standard error of the estimate
standard_error = np.std(residuals)

# Calculate the critical value for a 95% confidence interval
n = len(y_test_regression)  # Number of observations
alpha = 0.05  # Significance level
t_critical = stats.t.ppf(1 - alpha/2, df=n-1)  # Two-tailed t-distribution

# Calculate margin of error
margin_of_error = t_critical * standard_error

# Print margin of error
print(f"Margin of Error: {margin_of_error}")

# Plotting Logistic Regression Results (classification)
plt.figure(figsize=(10,6))
plt.scatter(X_test_classification[['Age', 'Glucose', 'BloodPressure']], y_test_classification, color='blue', label='Actual Outcome')
plt.scatter(X_test_classification['Age'], y_pred_classification, color='red', label='Predicted Outcome', marker='+')
plt.title('Logistic Regression: Actual vs Predicted Outcome')
plt.xlabel('Age')
plt.ylabel('Outcome')
plt.legend()
plt.show()

# Plotting Linear Regression Results (continuous prediction)
plt.figure(figsize=(10,6))
plt.scatter(X_test_regression['Age', 'Glucose', 'BloodPressure'], y_test_regression, color='blue', label='Actual Insulin')
plt.plot(X_test_regression['Age', 'Glucose', 'BloodPressure'], y_pred_regression, color='red', label='Predicted Insulin', linewidth=2)
plt.fill_between(X_test_regression['Age', 'Glucose', 'BloodPressure'], y_pred_regression - margin_of_error, y_pred_regression + margin_of_error, color='gray', alpha=0.5, label='Margin of Error')
plt.title('Linear Regression: Actual vs Predicted Insulin')
plt.xlabel('Age', 'Glucose', 'BloodPressure')
plt.ylabel('Insulin Level')
plt.legend()
plt.show()

# Parametric Test: T-test
group1 = data_cleaned[data_cleaned['Outcome'] == 1]['Glucose']  # Group with diabetes
group0 = data_cleaned[data_cleaned['Outcome'] == 0]['Glucose']  # Group without diabetes
t_stat, p_value_ttest = stats.ttest_ind(group1, group0)

print(f"T-test: t-statistic = {t_stat}, p-value = {p_value_ttest}")

# A/B Testing Example: Comparing Insulin levels based on Outcome
ab_test_group1 = data_cleaned[data_cleaned['Outcome'] == 1]['Insulin']
ab_test_group0 = data_cleaned[data_cleaned['Outcome'] == 0]['Insulin']
t_stat_ab, p_value_ab = stats.ttest_ind(ab_test_group1, ab_test_group0)

print(f"A/B Testing: t-statistic = {t_stat_ab}, p-value = {p_value_ab}")

# Chi-Square Test: Testing independence between two categorical variables
chi2_stat, p_value_chi2, dof, expected = stats.chi2_contingency(pd.crosstab(data_cleaned['Outcome'], data_cleaned['SkinThickness']))
print(f"Chi-Square Test: chi2-statistic = {chi2_stat}, p-value = {p_value_chi2}, degrees of freedom = {dof}")
