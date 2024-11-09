import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score, mean_squared_error
import matplotlib.pyplot as plt

# Generate synthetic healthcare data

# 1. Logistic Regression Example: Predicting if a patient has diabetes (binary classification)

# Sample healthcare data for logistic regression
data_logistic = {
    'Age': np.random.randint(20, 80, size=100),  # age of the patient
    'BMI': np.random.uniform(18, 35, size=100),  # body mass index
    'BloodSugarLevel': np.random.uniform(70, 180, size=100),  # blood sugar level
    'HasDiabetes': np.random.randint(0, 2, size=100)  # 0 = no, 1 = yes (target)
}

df_logistic = pd.DataFrame(data_logistic)

# Features and target for logistic regression
X_logistic = df_logistic[['Age', 'BMI', 'BloodSugarLevel']]
y_logistic = df_logistic['HasDiabetes']

# Split the data into training and testing sets
X_train_log, X_test_log, y_train_log, y_test_log = train_test_split(X_logistic, y_logistic, test_size=0.2, random_state=42)

# Train the logistic regression model
logreg_model = LogisticRegression()
logreg_model.fit(X_train_log, y_train_log)

# Predict on test data
y_pred_log = logreg_model.predict(X_test_log)

# Model accuracy
logistic_accuracy = accuracy_score(y_test_log, y_pred_log)
print(f"Logistic Regression Model Accuracy (Diabetes Prediction): {logistic_accuracy * 100:.2f}%")

# 2. Linear Regression Example: Predicting blood pressure (continuous regression)

# Sample healthcare data for linear regression
data_linear = {
    'Age': np.random.randint(20, 80, size=100),  # age of the patient
    'BMI': np.random.uniform(18, 35, size=100),  # body mass index
    'BloodPressure': np.random.uniform(90, 160, size=100)  # blood pressure (target)
}

df_linear = pd.DataFrame(data_linear)

# Features and target for linear regression
X_linear = df_linear[['Age', 'BMI']]
y_linear = df_linear['BloodPressure']

# Split the data into training and testing sets
X_train_lin, X_test_lin, y_train_lin, y_test_lin = train_test_split(X_linear, y_linear, test_size=0.2, random_state=42)

# Train the linear regression model
linreg_model = LinearRegression()
linreg_model.fit(X_train_lin, y_train_lin) 

# Predict on test data
y_pred_lin = linreg_model.predict(X_test_lin)

# Model performance (Mean Squared Error)
mse_linear = mean_squared_error(y_test_lin, y_pred_lin)
print(f"Linear Regression Model MSE (Blood Pressure Prediction): {mse_linear:.2f}")

# Plot for linear regression results
plt.scatter(df_linear['Age'], df_linear['BloodPressure'], color='blue', label='Actual Blood Pressure')
plt.scatter(X_test_lin['Age'], y_pred_lin, color='red', label='Predicted Blood Pressure')
plt.xlabel('Age')
plt.ylabel('Blood Pressure')
plt.legend()
plt.title('Actual vs Predicted Blood Pressure (Linear Regression)')
plt.show()
