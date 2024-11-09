# Let's first inspect the uploaded 'Metro_Interstate_Traffic_Volume.csv' file to understand its structure
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
file_path = 'C:\\Users\\ASUS\\Downloads\\Metro_Interstate_Traffic_Volume.csv'
traffic_df = pd.read_csv(file_path)

# Display the first few rows and column names to understand the dataset
print("First few rows of the dataset:")
print(traffic_df.head())
print("\nColumn names:")
print(traffic_df.columns)

# Describe the dataset
print("\nStatistical summary of the dataset:")
print(traffic_df.describe())
print("\nDataset Information:")
print(traffic_df.info())

# Replace null values in the 'holiday' column with 'No Holiday'
traffic_df['holiday'].fillna('No Holiday', inplace=True)

# Convert temperature from Kelvin to Celsius for better interpretability
traffic_df['temp_celsius'] = traffic_df['temp'] - 273.15

# Plot pair plots before removing outliers
print("\nPlotting pair plots before removing outliers...")
sns.pairplot(traffic_df, vars=['rain_1h', 'snow_1h', 'clouds_all', 'temp_celsius', 'traffic_volume'])
plt.suptitle('Pair Plots Before Removing Outliers', y=1.02)
plt.show()

# Remove the highest rain value
highest_rain_value = traffic_df['rain_1h'].max()
traffic_df = traffic_df[traffic_df['rain_1h'] != highest_rain_value]

# Remove outliers in temperature using IQR method
Q1_temp = traffic_df['temp_celsius'].quantile(0.25)
Q3_temp = traffic_df['temp_celsius'].quantile(0.75)
IQR_temp = Q3_temp - Q1_temp
lower_bound_temp = Q1_temp - 1.5 * IQR_temp
upper_bound_temp = Q3_temp + 1.5 * IQR_temp

# Filter out outliers in temperature
traffic_df = traffic_df[(traffic_df['temp_celsius'] >= lower_bound_temp) & (traffic_df['temp_celsius'] <= upper_bound_temp)]

# Print min and max temperatures after removing outliers
min_temp = traffic_df['temp_celsius'].min()
max_temp = traffic_df['temp_celsius'].max()
print(f"\nMinimum Temperature (Celsius) after removing outliers: {min_temp:.2f}")
print(f"Maximum Temperature (Celsius) after removing outliers: {max_temp:.2f}")

# Define columns for numeric variables
numeric_cols = ['rain_1h', 'snow_1h', 'clouds_all', 'temp_celsius']

# Use Label Encoding for categorical variables
label_encoder = LabelEncoder()
traffic_df['holiday'] = label_encoder.fit_transform(traffic_df['holiday'])
traffic_df['weather_main'] = label_encoder.fit_transform(traffic_df['weather_main'])
traffic_df['weather_description'] = label_encoder.fit_transform(traffic_df['weather_description'])

# Plot pair plots after converting categorical to numerical
print("\nPlotting pair plots after converting categorical to numerical...")
sns.pairplot(traffic_df, vars=numeric_cols + ['traffic_volume'])
plt.suptitle('Pair Plots After Converting Categorical to Numerical', y=1.02)
plt.show()

# Plot histograms for numeric variables in one figure
plt.figure(figsize=(12, 10))
for i, col in enumerate(numeric_cols):
    plt.subplot(2, 2, i + 1)  # Create a 2x2 grid for subplots
    sns.histplot(traffic_df[col], bins=30, kde=True)
    plt.title(f'Histogram of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# Scatter plot for temperature and traffic volume
plt.figure(figsize=(8, 6))
sns.scatterplot(x=traffic_df['temp_celsius'], y=traffic_df['traffic_volume'], alpha=0.5)
plt.title('Traffic Volume vs Temperature (Celsius)')
plt.xlabel('Temperature (Celsius)')
plt.ylabel('Traffic Volume')
plt.tight_layout()
plt.show()

# Prepare data for linear regression
X = traffic_df[numeric_cols + ['temp_celsius']]  # Features
y = traffic_df['traffic_volume']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

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

# Plotting Actual vs Predicted Traffic Volume
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')  # 45-degree line
plt.title('Actual vs Predicted Traffic Volume')
plt.xlabel('Actual Traffic Volume')
plt.ylabel('Predicted Traffic Volume')
plt.tight_layout()
plt.show()

# Correlation heatmap for numeric variables
print("\nPlotting correlation heatmap for numeric variables...")
plt.figure(figsize=(10, 8))
correlation_matrix = traffic_df[numeric_cols + ['traffic_volume']].corr()  # Include traffic_volume for correlation
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.3f', square=True)
plt.title("Correlation Heatmap (Numeric Variables)")
plt.show()
