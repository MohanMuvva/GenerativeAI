# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from scipy import stats

# Load the dataset
data = pd.read_csv('C:\\Users\\ASUS\\Downloads\\Titanic-Dataset.csv')

# 1. Describing the Dataset
print("Dataset Info:")
print(data.info())
print("\nDataset Description:")
print(data.describe())

# 2. Checking for Null Values
print("\nChecking for Null Values:")
print(data.isnull().sum())

# Handling missing values by filling with median for age (as an example)
if 'Age' in data.columns:
    data['Age'] = data['Age'].fillna(data['Age'].median())

# Dropping any remaining null values for simplicity
data.dropna(inplace=True)

# 3. Converting Categorical Values to Numerical (except 'Ticket')
# Using pd.get_dummies to one-hot encode categorical variables excluding 'Ticket'
categorical_columns = data.select_dtypes(include=['object']).columns
categorical_columns = [col for col in categorical_columns if col != 'Ticket']
data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)

# 4. Identifying Outliers
# Using Z-score method to identify outliers in the 'Age' column
if 'Age' in data.columns:
    z_scores = np.abs(stats.zscore(data['Age']))
    data = data[(z_scores < 3)]  # Retaining only data with Z-score < 3 (95% data)

# 5. Plotting Age vs. Survived in a histogram, clustered by Gender
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='Age', hue='Sex_male', bins=20, kde=False, multiple='stack')
plt.title('Distribution of Age by Gender')
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend(title='Gender', labels=['Female', 'Male'])
plt.show()

# Check the distribution of Survived by Gender to understand any imbalances
print("\nTotal count of males and females who survived:")
print(data.groupby('Sex_male')['Survived'].value_counts())

# Calculate the total count of males and females
total_males = data[data['Sex_male'] == 1].shape[0]
total_females = data[data['Sex_male'] == 0].shape[0]

# Calculate the count of survivors within each gender group
survived_males = data[(data['Sex_male'] == 1) & (data['Survived'] == 1)].shape[0]
survived_females = data[(data['Sex_male'] == 0) & (data['Survived'] == 1)].shape[0]

# Print these counts to cross-check
print(f"\nTotal males: {total_males}, Survived males: {survived_males}")
print(f"Total females: {total_females}, Survived females: {survived_females}")

# Re-calculate survival rates to ensure accurate values
male_survival_rate = (survived_males / total_males) * 100 if total_males > 0 else 0
female_survival_rate = (survived_females / total_females) * 100 if total_females > 0 else 0

# Output the survival rates by gender
print("\nSurvival Rates by Gender (verified):")
print(f"Male Survival Rate: {male_survival_rate:.2f}%")
print(f"Female Survival Rate: {female_survival_rate:.2f}%")

# 6. K-Means Clustering based on Pclass
if {'Pclass', 'Age', 'Fare'}.issubset(data.columns):
    # Selecting relevant features for clustering
    features_for_clustering = data[['Pclass', 'Age', 'Fare']]
    
    # Performing KMeans clustering with 3 clusters
    kmeans = KMeans(n_clusters=3, random_state=0)
    data['Pclass_cluster'] = kmeans.fit_predict(features_for_clustering)
    
    # Displaying the first few rows with the new cluster assignments
    print("\nData after adding clusters based on Pclass, Age, and Fare:")
    print(data[['Pclass', 'Age', 'Fare', 'Pclass_cluster']].head())


# 7. Plotting Age vs. Survived for each Pclass Cluster
for cluster in data['Pclass_cluster'].unique():
    cluster_data = data[data['Pclass_cluster'] == cluster]
    plt.figure(figsize=(8, 6))
    
    sns.boxplot(x='Survived', y='Age', data=cluster_data)
    plt.title(f'Age vs Survived for Pclass Cluster {cluster}')
    plt.xlabel('Survived (0 = No, 1 = Yes)')
    plt.ylabel('Age')
    plt.show()

# 8. Regression Analysis to Predict Survival Rate
# Preparing data for regression (assuming binary classification for survival)
if 'Survived' in data.columns:
    # Choosing features for prediction, now including one-hot encoded categorical variables
    features = [col for col in data.columns if col not in ['Survived', 'Ticket', 'PassengerId', 'Cabin']]
    X = data[features]
    y = data['Survived']

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Logistic Regression Model
    log_reg = LogisticRegression(max_iter=200)
    log_reg.fit(X_train, y_train)

    # Making predictions
    y_pred = log_reg.predict(X_test)

    # Evaluating the model
    print("\nRegression Analysis (Logistic Regression):")
    print("Accuracy Score:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
