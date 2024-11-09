import pandas as pd
from scipy.stats import chi2_contingency
import csv
# Load the dataset
file_path = 'C:\\Users\\ASUS\\genai\\module_5\\healthcare_dataset\\healthcare_dataset.csv'
df = pd.read_csv(file_path)

# Cleaning up the dataset: making 'Gender' and 'TestResults' columns consistent
df['Gender'] = df['Gender'].str.strip().str.lower().str.capitalize()
df['TestResults'] = df['TestResults'].str.strip().str.lower().str.capitalize()

# 1. Chi-Square Test: Gender vs. Test Results
# Create a contingency table
contingency_table_gender_test_results = pd.crosstab(df['Gender'], df['TestResults'])

# Apply Chi-Square test
chi2_gender, p_gender, dof_gender, expected_gender = chi2_contingency(contingency_table_gender_test_results)

# Print results for Gender vs. Test Results
print("Chi-Square Test: Gender vs. Test Results")
print(f"Chi2 Value: {chi2_gender}")
print(f"p-value: {p_gender}")
print(f"Degrees of Freedom: {dof_gender}")
print(f"Expected Frequencies: \n{expected_gender}\n")

# 2. A/B Testing: Medication Type (Ibuprofen vs. Aspirin) and Test Results
# Select rows where the medication is either Ibuprofen or Aspirin
df_medication_test = df[df['Medication'].isin(['Ibuprofen', 'Aspirin'])]

# Create a contingency table for Medication vs. Test Results
contingency_table_medication_test_results = pd.crosstab(df_medication_test['Medication'], df_medication_test['TestResults'])

# Apply Chi-Square test
chi2_medication, p_medication, dof_medication, expected_medication = chi2_contingency(contingency_table_medication_test_results)

# Print results for Medication vs. Test Results
print("Chi-Square Test: Medication (Ibuprofen vs. Aspirin) vs. Test Results")
print(f"Chi2 Value: {chi2_medication}")
print(f"p-value: {p_medication}")
print(f"Degrees of Freedom: {dof_medication}")
print(f"Expected Frequencies: \n{expected_medication}")
