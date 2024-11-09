import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset (replace the file path with your actual path)
file_path = 'C:\\Users\\ASUS\\Downloads\\Student_performance_data _.csv'
student_data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("Dataset Head:")
print(student_data.head())

# Print all columns in the DataFrame
print("\nAll columns in the dataset:")
print(student_data.columns.tolist())

# Display the basic information about the dataset
print("\nDataset Information:")
print(student_data.info())

# Display statistical summary of the dataset
print("\nStatistical summary of the dataset:")
print(student_data.describe())

# Summary statistics for 'GPA', 'StudyTimeWeekly', and 'Absences'
mean_values = student_data[['GPA', 'StudyTimeWeekly', 'Absences']].mean()
median_values = student_data[['GPA', 'StudyTimeWeekly', 'Absences']].median()
mode_values = student_data[['GPA', 'StudyTimeWeekly', 'Absences']].mode().iloc[0]
std_dev = student_data[['GPA', 'StudyTimeWeekly', 'Absences']].std()
min_values = student_data[['GPA', 'StudyTimeWeekly', 'Absences']].min()
max_values = student_data[['GPA', 'StudyTimeWeekly', 'Absences']].max()

print("\nMean:\n", mean_values)
print("\nMedian:\n", median_values)
print("\nMode:\n", mode_values)
print("\nStandard Deviation:\n", std_dev)
print("\nMin Values:\n", min_values)
print("\nMax Values:\n", max_values)

# Outlier detection based on standard deviation (we typically define outliers as more than 3 standard deviations from the mean)
outlier_threshold = 3  # Define threshold as 3 standard deviations from the mean

# Check for outliers (values outside the mean ± 3*SD)
outliers = student_data[
    (student_data['GPA'] > mean_values['GPA'] + outlier_threshold * std_dev['GPA']) |
    (student_data['GPA'] < mean_values['GPA'] - outlier_threshold * std_dev['GPA']) |
    (student_data['StudyTimeWeekly'] > mean_values['StudyTimeWeekly'] + outlier_threshold * std_dev['StudyTimeWeekly']) |
    (student_data['StudyTimeWeekly'] < mean_values['StudyTimeWeekly'] - outlier_threshold * std_dev['StudyTimeWeekly']) |
    (student_data['Absences'] > mean_values['Absences'] + outlier_threshold * std_dev['Absences']) |
    (student_data['Absences'] < mean_values['Absences'] - outlier_threshold * std_dev['Absences'])
]

print("\nOutliers based on standard deviation:\n", outliers)

# Heatmap Analysis
# Exclude 'StudentID' and 'Ethnicity' from the correlation matrix
correlation_matrix = student_data.drop(columns=['StudentID', 'Ethnicity']).corr()  # Adjust as necessary

# Plotting the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', square=True)
plt.title('Correlation Heatmap (Excluding StudentID and Ethnicity)')
plt.show()

# Scatter Plots for GPA against StudyTimeWeekly, Absences, and Tutoring
variables_to_plot = ['StudyTimeWeekly', 'Absences', 'Tutoring']

# Create scatter plots for GPA against each specified variable
for var in variables_to_plot:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=student_data, x=var, y='GPA')
    plt.title(f'Scatter Plot of GPA vs {var}')
    plt.xlabel(var)
    plt.ylabel('GPA')
    plt.grid()
    plt.show()

# Prepare the data for linear regression
X = student_data[['StudyTimeWeekly', 'Absences', 'Tutoring']]  # Independent variables
y = student_data['GPA']  # Dependent variable

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

# Plotting Actual vs Predicted GPA
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')  # 45-degree line
plt.title('Actual vs Predicted GPA')
plt.xlabel('Actual GPA')
plt.ylabel('Predicted GPA')
plt.grid()
plt.show()
