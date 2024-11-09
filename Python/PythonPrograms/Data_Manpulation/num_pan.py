import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# File path
file_path = 'C:\\Users\\ASUS\\gen-ai\\healthcare_dataset\\healthcare_dataset.csv'

# Load the dataset
df = pd.read_csv(file_path)

# Print basic information about the dataset
print(df.info())
print("\nFirst few rows of the dataset:")
print(df.head())

# Preprocessing
# Assuming 'Test_Results' is our target variable and it's categorical
# We'll encode it numerically
df['TestResults'] = pd.Categorical(df['TestResults']).codes

# Select features (you may need to adjust this based on your dataset)
features = ['Name','Age', 'Gender', 'BloodType', 'MedicalCondition', 'DateofAdmission', 'DoctorHospital', 'InsuranceProvider', 'BillingAmount', 'RoomNumber', 'AdmissionType', 'DischargeDate', 'Medication', 'TestResults']
X = df[features]
y = df['TestResults'].values

# Encode categorical variables
X = pd.get_dummies(X)

# Split the data
np.random.seed(42)
mask = np.random.rand(len(df)) < 0.8
X_train = X[mask]
X_test = X[~mask]
y_train = y[mask]
y_test = y[~mask]

# Scale the features
X_train = (X_train - X_train.mean()) / X_train.std()
X_test = (X_test - X_train.mean()) / X_train.std()

# Add intercept term
X_train = np.c_[np.ones(X_train.shape[0]), X_train]
X_test = np.c_[np.ones(X_test.shape[0]), X_test]

# Logistic Regression implementation
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def cost_function(X, y, theta):
    m = len(y)
    h = sigmoid(np.dot(X, theta))
    cost = (-1/m) * np.sum(y * np.log(h) + (1-y) * np.log(1-h))
    return cost

def gradient_descent(X, y, theta, alpha, num_iters):
    m = len(y)
    for _ in range(num_iters):
        h = sigmoid(np.dot(X, theta))
        gradient = np.dot(X.T, (h - y)) / m
        theta -= alpha * gradient
    return theta

# Train Logistic Regression
theta = np.zeros(X_train.shape[1])
alpha = 0.01
num_iters = 1000
theta = gradient_descent(X_train, y_train, theta, alpha, num_iters)

# Predict using Logistic Regression
y_pred_lr = sigmoid(np.dot(X_test, theta)) >= 0.5

# Decision Tree implementation
class DecisionTree:
    def __init__(self, max_depth=5):
        self.max_depth = max_depth
    
    def fit(self, X, y):
        self.tree = self._grow_tree(X, y)
    
    def _grow_tree(self, X, y, depth=0):
        num_samples, num_features = X.shape
        num_labels = len(np.unique(y))
        
        if depth >= self.max_depth or num_labels == 1 or num_samples < 2:
            return np.bincount(y).argmax()
        
        feature_idx, threshold = self._best_split(X, y)
        
        left_idxs = X[:, feature_idx] < threshold
        right_idxs = ~left_idxs
        
        left = self._grow_tree(X[left_idxs], y[left_idxs], depth+1)
        right = self._grow_tree(X[right_idxs], y[right_idxs], depth+1)
        
        return {'feature_idx': feature_idx, 'threshold': threshold, 'left': left, 'right': right}
    
    def _best_split(self, X, y):
        m = y.size
        if m <= 1:
            return None, None
        
        num_parent = [np.sum(y == c) for c in range(np.max(y) + 1)]
        best_gini = 1.0 - sum((n / m) ** 2 for n in num_parent)
        best_idx, best_thr = None, None
        
        for idx in range(X.shape[1]):
            thresholds, classes = zip(*sorted(zip(X[:, idx], y)))
            num_left = [0] * (np.max(y) + 1)
            num_right = num_parent.copy()
            for i in range(1, m):
                c = classes[i - 1]
                num_left[c] += 1
                num_right[c] -= 1
                gini_left = 1.0 - sum((num_left[x] / i) ** 2 for x in range(len(num_left)))
                gini_right = 1.0 - sum((num_right[x] / (m - i)) ** 2 for x in range(len(num_right)))
                gini = (i * gini_left + (m - i) * gini_right) / m
                if thresholds[i] == thresholds[i - 1]:
                    continue
                if gini < best_gini:
                    best_gini = gini
                    best_idx = idx
                    best_thr = (thresholds[i] + thresholds[i - 1]) / 2
        return best_idx, best_thr
    
    def predict(self, X):
        return np.array([self._predict_tree(x, self.tree) for x in X])
    
    def _predict_tree(self, x, node):
        if isinstance(node, dict):
            if x[node['feature_idx']] < node['threshold']:
                return self._predict_tree(x, node['left'])
            else:
                return self._predict_tree(x, node['right'])
        return node

# Train Decision Tree
dt = DecisionTree(max_depth=5)
dt.fit(X_train[:, 1:], y_train)  # Exclude the intercept term for Decision Tree

# Predict using Decision Tree
y_pred_dt = dt.predict(X_test[:, 1:])  # Exclude the intercept term for Decision Tree

# Evaluate models
def accuracy(y_true, y_pred):
    return np.mean(y_true == y_pred)

print("\nLogistic Regression Accuracy:", accuracy(y_test, y_pred_lr))
print("Decision Tree Accuracy:", accuracy(y_test, y_pred_dt))

# Visualize results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.bar(['Logistic Regression', 'Decision Tree'], [accuracy(y_test, y_pred_lr), accuracy(y_test, y_pred_dt)])
plt.title('Model Accuracy Comparison')
plt.ylabel('Accuracy')

plt.subplot(1, 2, 2)
plt.scatter(X_test[:, 1], X_test[:, 2], c=y_test, cmap='viridis')
plt.title('Test Data Distribution')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

plt.tight_layout()
plt.show()

