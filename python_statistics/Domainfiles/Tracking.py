import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

# Load the dataset
file_path = 'C:\\Users\\ASUS\\Downloads\\dailyActivity_merged.csv'  # Update with your actual file path
df = pd.read_csv(file_path)

# 1. Check for null values
print("Checking for null values:")
null_values = df.isnull().sum()
print(null_values)

# 2. Describe the dataset
print("\nData Description:")
data_description = df.describe()
print(data_description)

# 3. Basic dataset information
print("\nDataset Info:")
df.info()

# 4. Convert categorical variables to numerical
# Identify categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns

# Apply Label Encoding to categorical columns
label_encoder = LabelEncoder()
for col in categorical_cols:
    df[col] = label_encoder.fit_transform(df[col])

# 5. Identify and replace outliers in VeryActiveDistance and ModeratelyActiveDistance
def replace_outliers_with_mean(column):
    # Calculate Q1 (25th percentile) and Q3 (75th percentile)
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1  # Interquartile range

    # Define outlier bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Calculate mean and median excluding outliers
    mean_value = column[(column >= lower_bound) & (column <= upper_bound)].mean()
    median_value = column[(column >= lower_bound) & (column <= upper_bound)].median()

    # Replace outliers with mean
    column = column.where((column >= lower_bound) & (column <= upper_bound), mean_value)
    
    return column, mean_value, median_value

# Replace outliers for VeryActiveDistance and ModeratelyActiveDistance
df['VeryActiveDistance'], very_active_mean, very_active_median = replace_outliers_with_mean(df['VeryActiveDistance'])
df['ModeratelyActiveDistance'], moderately_active_mean, moderately_active_median = replace_outliers_with_mean(df['ModeratelyActiveDistance'])

# Print calculated means and medians
print(f"\nVeryActiveDistance - Mean: {very_active_mean:.2f}, Median: {very_active_median:.2f}")
print(f"ModeratelyActiveDistance - Mean: {moderately_active_mean:.2f}, Median: {moderately_active_median:.2f}")

# 6. Prepare the data for correlation analysis
# Exclude specified columns and include all others
features_for_correlation = df.drop(columns=['ActivityDate', 'TotalDistance', 'TrackerDistance', 'Id',])

# Correlation heatmap for the selected columns
print("\nPlotting correlation heatmap for selected features...")
plt.figure(figsize=(12, 8))
correlation_matrix = features_for_correlation.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap (Selected Features)")
plt.show()

# 7. Box plots for all relevant columns
relevant_columns = df.drop(columns=['ActivityDate', 'TotalDistance', 'Calories', 'TrackerDistance', 'Id', 'LoggedActivitiesDistance', 'VeryActiveMinutes', 'FairlyActiveMinutes', 'SedentaryActiveDistance']).columns

for col in relevant_columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(y=df[col])
    plt.title(f'Boxplot of {col}')
    plt.ylabel(col)
    plt.grid()
    plt.show()

# 8. Prepare the data for linear regression
features = df.drop(columns=['ActivityDate', 'TotalDistance', 'TrackerDistance', 'Id', 'Calories', 'LoggedActivitiesDistance', 'VeryActiveMinutes', 'FairlyActiveMinutes', 'SedentaryActiveDistance'])  # Exclude specified columns
target = df['Calories']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42)

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nLinear Regression Model Evaluation:")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R^2 Score: {r2:.2f}")

# Print model coefficients
print("\nModel Coefficients:")
for i, col in enumerate(features.columns):
    print(f"{col}: {model.coef_[i]:.2f}")

# 9. Plotting the Linear Regression Model
# Create a DataFrame for plotting actual vs predicted
predicted_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

# Plotting Actual vs Predicted
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Actual', y='Predicted', data=predicted_df, alpha=0.6)
plt.plot([predicted_df['Actual'].min(), predicted_df['Actual'].max()],
         [predicted_df['Actual'].min(), predicted_df['Actual'].max()],
         color='red', linestyle='--')  # 45-degree line
plt.title('Actual vs Predicted Calories')
plt.xlabel('Actual Calories')
plt.ylabel('Predicted Calories')
plt.grid()
plt.show()
