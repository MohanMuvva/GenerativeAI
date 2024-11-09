# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the Iris dataset
iris = datasets.load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target

# Convert categorical data to numerical using Label Encoding (for compatibility)
label_encoder = LabelEncoder()
iris_df['species'] = label_encoder.fit_transform(iris_df['species'])

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(iris_df.head())

# 1. Basic Information and Descriptive Statistics
print("\nDataset Info:")
print(iris_df.info())
print("\nDescriptive Statistics:")
print(iris_df.describe())

# 2. Checking for Null Values
print("\nChecking for Null Values:")
print(iris_df.isnull().sum())

# 3. Visualizing the Distribution of Features
sns.pairplot(iris_df, hue='species', markers=['o', 's', 'D'], palette='viridis')
plt.suptitle("Pairplot of Iris Dataset Features", y=1.02)
plt.show()

# 4. Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(iris_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap of Iris Dataset")
plt.show()

# 5. Principal Component Analysis (PCA) for Dimensionality Reduction
# Standardize the data
features = iris_df.drop(columns=['species'])
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Apply PCA
pca = PCA(n_components=2)  # Reducing to 2 dimensions
principal_components = pca.fit_transform(scaled_features)

# Creating a DataFrame with the PCA results
pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
pca_df['species'] = iris_df['species']

# Explained Variance by each Principal Component
print("\nExplained Variance Ratio by each Principal Component:")
print(pca.explained_variance_ratio_)

# Visualizing the PCA result
plt.figure(figsize=(10, 6))
sns.scatterplot(data=pca_df, x='PC1', y='PC2', hue='species', palette='viridis', s=100)
plt.title("PCA of Iris Dataset")
plt.xlabel(f"Principal Component 1 ({pca.explained_variance_ratio_[0]:.2%} variance)")
plt.ylabel(f"Principal Component 2 ({pca.explained_variance_ratio_[1]:.2%} variance)")
plt.legend(title='Species')
plt.show()

# 6. KMeans Clustering Based on PCA Components
# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=0)
pca_df['cluster'] = kmeans.fit_predict(principal_components)

# Visualizing KMeans Clustering Results
plt.figure(figsize=(10, 6))
sns.scatterplot(data=pca_df, x='PC1', y='PC2', hue='cluster', palette='cool', style='species', s=100)
plt.title("KMeans Clustering on PCA-Reduced Iris Dataset")
plt.xlabel(f"Principal Component 1 ({pca.explained_variance_ratio_[0]:.2%} variance)")
plt.ylabel(f"Principal Component 2 ({pca.explained_variance_ratio_[1]:.2%} variance)")
plt.legend(title='Cluster')
plt.show()

# 7. Logistic Regression Model to Predict Species
# Splitting the dataset into training and test sets
X = iris_df.drop(columns=['species'])
y = iris_df['species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a logistic regression model
log_reg = LogisticRegression(max_iter=200)
log_reg.fit(X_train, y_train)

# Making predictions
y_pred = log_reg.predict(X_test)

# Model evaluation
print("\nLogistic Regression Model Evaluation:")
print("Accuracy Score:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Visualizing Confusion Matrix
plt.figure(figsize=(6, 4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title("Confusion Matrix")
plt.xlabel("Predicted Labels")
plt.ylabel("True Labels")
plt.show()

# 8. K-Fold Cross-Validation on Logistic Regression Model
# Preparing features and target for K-Fold
X_pca = pca_df[['PC1', 'PC2']]
y_pca = pca_df['species']

# Initialize the Logistic Regression model
model = LogisticRegression(max_iter=1000)

# Setting up K-Fold Cross-Validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)  # 5-fold cross-validation

# Performing K-Fold Cross-Validation
cv_scores = cross_val_score(model, X_pca, y_pca, cv=kf)

# Displaying the results
print("\nK-Fold Cross-Validation Scores for each fold:", cv_scores)
print("Mean Accuracy:", np.mean(cv_scores))
print("Standard Deviation:", np.std(cv_scores))
