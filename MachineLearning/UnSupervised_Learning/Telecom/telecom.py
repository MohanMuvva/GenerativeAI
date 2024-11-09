# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the dataset
data = pd.read_csv('C:\\Users\\ASUS\\Downloads\\telecom_churn.csv')  # Ensure correct file path

# Data Description
print("First few rows of the dataset:\n", data.head())
print("\nData types and missing values:\n", data.info())
print("\nStatistical Summary:\n", data.describe())
print("\nMissing values:\n", data.isnull().sum())

# Encode categorical variables
for column in data.select_dtypes(include=['object']).columns:
    data[column] = LabelEncoder().fit_transform(data[column])

# Define features (X) and target (y)
target_column = 'Churn'
X = data.drop(columns=[target_column])
y = data[target_column]

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Step 1: Standardize the training and test data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 2: Apply PCA on the training data to retain 95% variance
pca_train = PCA(n_components=0.95)
X_train_pca = pca_train.fit_transform(X_train_scaled)
X_test_pca = pca_train.transform(X_test_scaled)

print(f"\nNumber of PCA components to retain 95% variance: {pca_train.n_components_}")
print("Explained variance by each component:", pca_train.explained_variance_ratio_)
print("Total variance explained:", sum(pca_train.explained_variance_ratio_))

# Step 3: K-Means Clustering on the PCA-transformed training data
# Determine optimal number of clusters (k) using the Elbow method
wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=1)
    kmeans.fit(X_train_pca)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method for Optimal Number of Clusters')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Within-Cluster Sum of Squares (WCSS)')
plt.show()

# Fit KMeans with an optimal number of clusters, say 3 based on elbow plot
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=1)
train_clusters = kmeans.fit_predict(X_train_pca)

# Step 4: Logistic Regression Model with K-Fold Cross-Validation on Training Data
kf = KFold(n_splits=5, shuffle=True, random_state=1)
model = LogisticRegression()

# Perform cross-validation
cv_scores = cross_val_score(model, X_train_pca, y_train, cv=kf, scoring='accuracy')
mean_cv_score = np.mean(cv_scores)
print("\nCross-validated Accuracy scores:", cv_scores)
print("Mean Cross-Validation Accuracy:", mean_cv_score)

# Step 5: Train the final model and test it on the test data
# Train the model on the full training set
model.fit(X_train_pca, y_train)

# Predict on test set and evaluate
y_pred = model.predict(X_test_pca)
print("\nTest Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 6: 3D Visualization of clusters in training data (using first 3 PCA components)
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_train_pca[:, 0], X_train_pca[:, 1], X_train_pca[:, 2], c=train_clusters, cmap='viridis', s=50)
ax.set_title('3D PCA Cluster Visualization (Training Data)')
ax.set_xlabel('Principal Component 1')
ax.set_ylabel('Principal Component 2')
ax.set_zlabel('Principal Component 3')
plt.show()
