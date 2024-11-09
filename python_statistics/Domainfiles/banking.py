import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# Load the dataset
file_path = 'C:\\Users\\ASUS\\Downloads\\Loan_default_randomized.csv'  # Update this with your file path

# Attempt to read the CSV file
try:
    df = pd.read_csv(file_path)
except Exception as e:
    print(f"Error reading the CSV file: {e}")
    df = None

# Check if the DataFrame is loaded correctly
if df is not None:
    # 1. Check for null values
    print("Checking for null values:")
    null_values = df.isnull().sum()
    print(null_values)

    # 2. Check for duplicates
    def check_and_remove_duplicates(data):
        duplicates = data.duplicated().sum()
        if duplicates > 0:
            print(f"\nFound {duplicates} duplicate rows. Removing duplicates.")
            data.drop_duplicates(inplace=True)
        else:
            print("\nNo duplicate rows found.")
    
    check_and_remove_duplicates(df)

    # 3. Describe the dataset
    print("\nData Description:")
    data_description = df.describe()
    print(data_description)

    # 4. Basic dataset information
    print("\nDataset Info:")
    df.info()

    # 5. Convert all object/categorical columns to numerical values using Label Encoding
    label_encoder = LabelEncoder()
    for col in df.select_dtypes(include=['object']).columns:
        print(f"Converting {col} to numerical values using Label Encoding...")
        df[col] = label_encoder.fit_transform(df[col])

    # Ensure 'Default' is binary (for logistic regression)
    if df['Default'].nunique() > 2:
        print("Warning: Converting 'Default' to binary.")
        df['Default'] = df['Default'].apply(lambda x: 1 if x > 0.5 else 0)
        
    # Verify data after encoding
    print("\nData after encoding:")
    print(df.head())

    # 6. Exploratory Data Analysis (EDA)
    # Box plots with Default on the Y-axis
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='LoanAmount', y='Default')
    plt.title("Loan Amount vs. Default Status")
    plt.xlabel("Loan Amount")
    plt.ylabel("Default Status")
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='CreditScore', y='Default')
    plt.title("Credit Score vs. Default Status")
    plt.xlabel("Credit Score")
    plt.ylabel("Default Status")
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='Income', y='Default')
    plt.title("Income vs. Default Status")
    plt.xlabel("Income")
    plt.ylabel("Default Status")
    plt.show()

    # 7. Correlation matrix
    print("\nCalculating and plotting the correlation matrix...")
    correlation_matrix = df.select_dtypes(include=['float64', 'int64']).corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.3f')
    plt.title("Correlation Matrix")
    plt.show()

    # Prepare data for model
    X = df.drop(columns=['LoanID','Default'])
    y = df['Default']

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Logistic Regression Model
    model = LogisticRegression()
    model.fit(X_train_scaled, y_train)

    # Make predictions
    predictions = model.predict(X_test_scaled)

    # Calculate accuracy
    print("Accuracy:", accuracy_score(y_test, predictions))
else:
    print("DataFrame is empty. Please check the CSV file.")
