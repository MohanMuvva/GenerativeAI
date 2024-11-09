import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# File path
file_path = 'C:\\Users\\ASUS\\genai\\module_5\\healthcare_dataset\\healthcare_dataset.csv'

# Load the dataset
data = pd.read_csv(file_path)

# Preprocessing: Convert 'MedicalCondition' to a binary target variable
data['Diabetes'] = np.where(data['MedicalCondition'] == 'Diabetes', 1, 0)

# Select features for prediction
features = ['Age', 'Gender', 'BloodType', 'TestResults']
X = data[features]
y = data['Diabetes']

# Encode categorical variables
X = pd.get_dummies(X, drop_first=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Now let's check the distribution of the key features for Bayesian Inference
diabetes_data = data[data['MedicalCondition'] == 'Diabetes']
non_diabetes_data = data[data['MedicalCondition'] != 'Diabetes']

# Get the prior probability of having diabetes
P_diabetes = len(diabetes_data) / len(data)
P_no_diabetes = 1 - P_diabetes

# Calculate the distribution of categorical variables for both diabetes and non-diabetes patients
diabetes_age_dist = pd.cut(diabetes_data['Age'], bins=[0, 30, 50, 70, 100], labels=['Young', 'Middle-aged', 'Senior', 'Elderly']).value_counts(normalize=True)
non_diabetes_age_dist = pd.cut(non_diabetes_data['Age'], bins=[0, 30, 50, 70, 100], labels=['Young', 'Middle-aged', 'Senior', 'Elderly']).value_counts(normalize=True)

# Gender distribution
diabetes_gender_dist = diabetes_data['Gender'].value_counts(normalize=True)
non_diabetes_gender_dist = non_diabetes_data['Gender'].value_counts(normalize=True)

# BloodType distribution
diabetes_bloodtype_dist = diabetes_data['BloodType'].value_counts(normalize=True)
non_diabetes_bloodtype_dist = non_diabetes_data['BloodType'].value_counts(normalize=True)

# TestResults distribution
diabetes_testresults_dist = diabetes_data['TestResults'].value_counts(normalize=True)
non_diabetes_testresults_dist = non_diabetes_data['TestResults'].value_counts(normalize=True)

results = {
    "P_diabetes": P_diabetes,
    "P_no_diabetes": P_no_diabetes,
    "diabetes_age_dist": diabetes_age_dist,
    "non_diabetes_age_dist": non_diabetes_age_dist,
    "diabetes_gender_dist": diabetes_gender_dist,
    "non_diabetes_gender_dist": non_diabetes_gender_dist,
    "diabetes_bloodtype_dist": diabetes_bloodtype_dist,
    "non_diabetes_bloodtype_dist": non_diabetes_bloodtype_dist,
    "diabetes_testresults_dist": diabetes_testresults_dist,
    "non_diabetes_testresults_dist": non_diabetes_testresults_dist
}

print(results)

# Calculate the probability of diabetes given the test results
test_results_probabilities = {}
for test_result in diabetes_data['TestResults'].unique():
    # Count the number of diabetes cases for each test result
    diabetes_count = diabetes_data[diabetes_data['TestResults'] == test_result].shape[0]
    # Count the total number of cases for each test result (diabetes + non-diabetes)
    total_count = data[data['TestResults'] == test_result].shape[0]
    # Calculate the probability
    probability = diabetes_count / total_count if total_count > 0 else 0
    test_results_probabilities[test_result] = probability

# Print the probabilities
print("Probability of diabetes given the test results:")
for test_result, probability in test_results_probabilities.items():
    print(f"Test Result: {test_result}, Probability of Diabetes: {probability:.4f}")

