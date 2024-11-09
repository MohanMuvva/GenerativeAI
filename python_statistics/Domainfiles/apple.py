import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from scipy.stats import zscore

# Load the dataset
file_path = 'C:\\Users\\ASUS\\Downloads\\apple_quality.csv'  # Adjust file path as needed
df = pd.read_csv(file_path)

# Display the first few rows, info, and summary statistics
print("First few rows of the dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nDataset Description:")
print(df.describe(include='all'))

# Handle missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

for col in df.select_dtypes(include=['object']).columns:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Convert categorical columns to numerical using One-Hot Encoding
df = pd.get_dummies(df, drop_first=True)

# Check for duplicates and remove them if they exist
df.drop_duplicates(inplace=True)

# Strip leading/trailing spaces from text data (if any)
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# Check for any remaining missing values
print("\nMissing values per column after handling:")
print(df.isnull().sum())

# Rename columns to ensure consistent formatting
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Outlier Detection using Z-score
outliers = {}
for col in df.select_dtypes(include=[np.number]).columns:
    z_scores = zscore(df[col])
    outliers[col] = np.where(np.abs(z_scores) > 3)[0]  # Indices of outliers with z > 3

print("\nOutliers detected:")
for col, indices in outliers.items():
    if len(indices) > 0:
        print(f"Outliers in {col}: {indices}")
    else:
        print(f"No significant outliers in {col}.")

# Exploratory Data Analysis (EDA) with visualizations
# Histograms for each numerical column
df.hist(bins=15, figsize=(15, 10), color='skyblue')
plt.suptitle("Histograms of Numerical Columns")
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# Box plots to visualize outliers
plt.figure(figsize=(15, 10))
for i, col in enumerate(df.select_dtypes(include=[np.number]).columns, 1):
    plt.subplot(3, 4, i)
    sns.boxplot(df[col])
    plt.title(f"Boxplot of {col}")
plt.tight_layout()
plt.show()

# Correlation heatmap excluding 'a_id'
if 'a_id' in df.columns:
    df_no_id = df.drop(columns=['a_id'])
else:
    df_no_id = df

plt.figure(figsize=(12, 8))
sns.heatmap(df_no_id.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.show()

# Logistic Regression Analysis for Predicting 'quality'
# Ensure 'quality' is in numeric format, or convert it if it's categorical
if df['quality'].dtype == 'object':
    df['quality'] = pd.factorize(df['quality'])[0]

# Define features (X) and target (y), excluding 'a_id'
X = df_no_id.drop(columns=['quality'])
y = df['quality']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions and model evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("\nLogistic Regression Model Evaluation:")
print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion matrix visualization
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.show()
