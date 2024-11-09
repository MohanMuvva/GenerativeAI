import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from math import log2

# Load dataset
file_path = 'C:\\Users\\ASUS\\genai\\module_5\\healthcare_dataset\\healthcare_dataset.csv'
data = pd.read_csv(file_path)

# Preprocessing: Convert target variable 'MedicalCondition' to a binary target for diabetes
data['Diabetes'] = np.where(data['MedicalCondition'] == 'Diabetes', 1, 0)

# Select features for prediction (for simplicity, we'll use some example features)
features = ['Age', 'Gender', 'BloodType', 'TestResults']
X = data[features]
y = data['Diabetes']

# Convert categorical variables to numerical using one-hot encoding
X = pd.get_dummies(X, drop_first=True)

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

### 1. Calculate Entropy of Target Variable (Diabetes)
def calculate_entropy(y):
    # Calculate the proportion of each class (0 and 1)
    p1 = np.mean(y)  # Proportion of 1 (diabetic)
    p0 = 1 - p1      # Proportion of 0 (non-diabetic)
    
    # Calculate entropy
    if p1 == 0 or p0 == 0:  # If there is no uncertainty
        return 0
    entropy = - (p1 * log2(p1) + p0 * log2(p0))
    return entropy

# Entropy of the entire dataset
dataset_entropy = calculate_entropy(y_train)
print(f"Entropy of the dataset: {dataset_entropy:.4f}")

### 2. Sensitivity (Recall)
# Train a simple model (we'll use a decision tree as an example)
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Confusion Matrix
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

# Calculate Sensitivity
sensitivity = tp / (tp + fn)
print(f"Sensitivity: {sensitivity:.4f}")

### 3. Information Gain Calculation for Each Feature
# Calculate information gain for each feature
def calculate_information_gain(X, y, feature):
    # Calculate the entropy of the whole dataset
    parent_entropy = calculate_entropy(y)
    
    # Split dataset based on the feature
    values = X[feature].unique()
    weighted_entropy = 0
    
    for val in values:
        subset = y[X[feature] == val]
        weighted_entropy += len(subset) / len(y) * calculate_entropy(subset)
    
    # Information gain is the difference between parent entropy and weighted entropy of child nodes
    information_gain = parent_entropy - weighted_entropy
    return information_gain

# Calculate information gain for each feature in the dataset
for feature in X.columns:
    ig = calculate_information_gain(X_train, y_train, feature)
    print(f"Information Gain for {feature}: {ig:.4f}")
