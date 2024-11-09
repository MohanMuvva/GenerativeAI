import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load the dataset
file_path = 'C:\\Users\\ASUS\\Downloads\\updated_ecommerce_dataset.csv'  # Update this with your file path
df = pd.read_csv(file_path)

# 1. Check for null values
print("Checking for null values:")
null_values = df.isnull().sum()
print(null_values)

# 2. Identify categorical columns
categorical_cols = df.select_dtypes(include=['object', 'category']).columns

# 3. Label Encoding for categorical variables
# Initialize the LabelEncoder
label_encoder = LabelEncoder()

# Apply label encoding to categorical columns
for col in categorical_cols:
    df[col] = label_encoder.fit_transform(df[col].astype(str))  # Convert to string to avoid errors

# Optionally, you can check the unique values after encoding
print("\nUnique values after label encoding:")
for col in categorical_cols:
    print(f"{col}: {df[col].unique()}")

# 4. Convert remaining object types to numeric types where applicable
# Attempt to convert all object types to numeric, coercing errors
for col in df.select_dtypes(include=['object']).columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 5. Describe the dataset
print("\nData Description:")
data_description = df.describe()
print(data_description)

# 6. Basic dataset information
print("\nDataset Info:")
df.info()

# 7. Prepare data for logistic regression
# Assuming 'target' is the name of the target variable you want to predict
target_column = 'Purchased'  # Replace with your actual target column name
X = df.drop(columns=[target_column])  # Features
y = df[target_column]  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 8. Train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# 9. Make predictions
y_pred = model.predict(X_test)

# 10. Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print("\nModel Evaluation:")
print(f"Accuracy: {accuracy:.2f}")
print("\nConfusion Matrix:")
print(conf_matrix)
print("\nClassification Report:")
print(class_report)

# 11. Exploratory Data Analysis (EDA)
# Histograms for numeric columns
print("\nPlotting histograms for numerical features...")
df.hist(bins=20, figsize=(14, 10))
plt.tight_layout()
plt.show()

# Correlation Heatmap
print("\nPlotting correlation heatmap...")
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.3f')
plt.title("Correlation Heatmap")
plt.show()

# Count plot for categorical variables (if any)
for col in categorical_cols:
    plt.figure(figsize=(8, 4))
    sns.countplot(x=col, data=df)
    plt.title(f"Count Plot for {col}")
    plt.xticks(rotation=45)
    plt.show()

