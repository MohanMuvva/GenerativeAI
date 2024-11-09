import pandas as pd

# Load the dataset
file_path = 'C:\\Users\\ASUS\\genai\\module_5\\healthcare_dataset\\healthcare_dataset.csv'
df = pd.read_csv(file_path)

# Clean the dataset: Ensure consistent formatting
df['Gender'] = df['Gender'].str.strip().str.lower().str.capitalize()
df['TestResults'] = df['TestResults'].str.strip().str.lower().str.capitalize()
df['Medication'] = df['Medication'].str.strip().str.lower().str.capitalize()

# Create a contingency table for Gender and Test Results
contingency_table_gender_test = pd.crosstab(df['Gender'], df['TestResults'])
print("Contingency Table for Gender and Test Results:")
print(contingency_table_gender_test)

# Calculate the overall proportion of positive test results by Gender
total_positive = contingency_table_gender_test.loc[:, 'Positive'].sum()
total_negative = contingency_table_gender_test.loc[:, 'Negative'].sum()
total_males = contingency_table_gender_test.loc['Male'].sum()
total_females = contingency_table_gender_test.loc['Female'].sum()

# Overall proportions
overall_positive_male = contingency_table_gender_test.loc['Male', 'Positive'] / total_males
overall_positive_female = contingency_table_gender_test.loc['Female', 'Positive'] / total_females

print(f"\nOverall Proportion of Positive Test Results:")
print(f"Male: {overall_positive_male:.2f}")
print(f"Female: {overall_positive_female:.2f}")

# Now, analyze the relationship controlling for Medication
contingency_table_medication = pd.crosstab(df['Medication'], df['TestResults'])
print("\nContingency Table for Medication and Test Results:")
print(contingency_table_medication)

# Calculate proportions for each medication type
for medication in df['Medication'].unique():
    if medication:  # Check if medication is not NaN
        total_medication = contingency_table_medication.loc[medication].sum()
        positive_count = contingency_table_medication.loc[medication, 'Positive']
        positive_proportion = positive_count / total_medication
        print(f"Proportion of Positive Test Results for {medication}: {positive_proportion:.2f}")

# Analyze the relationship between Gender and Test Results within each Medication group
for medication in df['Medication'].unique():
    if medication:  # Check if medication is not NaN
        subset = df[df['Medication'] == medication]
        contingency_table_gender_test_medication = pd.crosstab(subset['Gender'], subset['TestResults'])
        print(f"\nContingency Table for Gender and Test Results (Medication: {medication}):")
        print(contingency_table_gender_test_medication)

        # Calculate proportions for this subset
        total_males = contingency_table_gender_test_medication.loc['Male'].sum()
        total_females = contingency_table_gender_test_medication.loc['Female'].sum()
        positive_male = contingency_table_gender_test_medication.loc['Male', 'Positive']
        positive_female = contingency_table_gender_test_medication.loc['Female', 'Positive']

        if total_males > 0:
            male_positive_proportion = positive_male / total_males
        else:
            male_positive_proportion = 0

        if total_females > 0:
            female_positive_proportion = positive_female / total_females
        else:
            female_positive_proportion = 0

        print(f"Proportion of Positive Test Results for Males: {male_positive_proportion:.2f}")
        print(f"Proportion of Positive Test Results for Females: {female_positive_proportion:.2f}")

print("\nInterpretation:")
print("If the overall proportions of positive test results show one trend (e.g., males have a higher proportion of positive results),")
print("but the proportions within each medication group show the opposite trend (e.g., females have a higher proportion of positive results),")
print("this is an example of Simpson's Paradox.")
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
