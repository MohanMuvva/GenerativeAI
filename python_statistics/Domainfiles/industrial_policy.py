import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
file_path = 'C:\\Users\\ASUS\\Downloads\\Industrial_Policy_Dataset.csv'  # Update with your actual file path
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

# 4. Exploratory Data Analysis (EDA)
# Filter out non-numeric columns for the correlation matrix
numeric_df = df.select_dtypes(include=['float64', 'int64'])

# Correlation matrix for numeric columns only
print("\nPlotting correlation heatmap...")
plt.figure(figsize=(8, 6))
correlation_matrix = numeric_df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap")
plt.show()

# Check the column names to find the correct industry column
print("\nColumn names in the DataFrame:")
print(df.columns)

# Pairplot to visualize the relationships between numerical variables, colored by industry
# Replace 'Industry Name' with the actual column name for industries
industry_column = 'Industry Name'  # Updated to 'Industry Name'

if industry_column in df.columns:
    print("\nGenerating pairplot for numerical features with industry differentiation...")
    sns.pairplot(df, hue=industry_column)  # Use the correct column name for industries
    plt.show()
else:
    print(f"Error: '{industry_column}' column not found in the DataFrame.")

# 5. Plotting Investment vs Production Output
# Ensure the column names match exactly with those in your DataFrame
investment_col = 'Investment (in Million INR)'  # Replace with the actual column name if different
production_output_col = 'Production Output (in Million INR)'  # Replace with the actual column name if different

# Check if the columns exist in the DataFrame
if investment_col in df.columns and production_output_col in df.columns:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=df[investment_col], y=df[production_output_col], hue=df[industry_column], alpha=0.6)  # Add hue for industry
    plt.title('Investment vs Production Output by Industry')
    plt.xlabel('Investment (in Million INR)')
    plt.ylabel('Production Output (in Million INR)')
    plt.grid()
    plt.legend(title='Industry')
    plt.show()
else:
    print(f"Columns '{investment_col}' or '{production_output_col}' not found in the DataFrame.")

# 6. Separate graphs for each industry
for industry in df[industry_column].unique():  # Use the correct column name for industries
    industry_data = df[df[industry_column] == industry]
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=industry_data[investment_col], y=industry_data[production_output_col], alpha=0.6)
    plt.title(f'Investment vs Production Output for {industry}')
    plt.xlabel('Investment (in Million INR)')
    plt.ylabel('Production Output (in Million INR)')
    plt.grid()
    plt.show()

# Define the features and target variable
features = ['Investment (in Million INR)', 'Employment Rate (%)', 'Infrastructure Score', 
            'Energy Consumption (in GWh)', 'Government Incentives (in Million INR)']
target = 'Production Output (in Million INR)'
industry_column = 'Industry Name'  # Update this if the column name is different

# Check if the necessary columns exist
if all(col in df.columns for col in features) and target in df.columns and industry_column in df.columns:
    # Loop through each unique industry
    for industry in df[industry_column].unique():
        print(f"\nProcessing industry: {industry}")
        
        # Filter the data for the current industry
        industry_data = df[df[industry_column] == industry]
        
        # Define features and target for the current industry
        X = industry_data[features]
        y = industry_data[target]
        
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
        
        print(f"Model Evaluation for {industry}:")
        print(f"Mean Squared Error: {mse:.2f}")
        print(f"R^2 Score: {r2:.2f}")
        
        # Plotting Actual vs Predicted values
        plt.figure(figsize=(10, 6))
        plt.scatter(y_test, y_pred, alpha=0.6)
        plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')  # 45-degree line
        plt.title(f'Actual vs Predicted Production Output for {industry}')
        plt.xlabel('Actual Production Output (in Million INR)')
        plt.ylabel('Predicted Production Output (in Million INR)')
        plt.grid()
        plt.show()
else:
    print("Error: One or more required columns are not found in the DataFrame.")
