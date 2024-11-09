# Banking Loan Default Prediction

This script is designed to process banking data for predicting loan defaults. It covers data loading, preprocessing, exploratory analysis, and model training using logistic regression.

## Features of the Script

- **Data Loading and Preprocessing**:
  - The dataset is loaded from a CSV file.
  - Null values and duplicates are identified and handled appropriately.
  - Categorical variables are converted to numerical using Label Encoding.

- **Exploratory Data Analysis (EDA)**:
  - Box plots are generated to visualize the relationship between loan amount, credit score, income, and default status.
  - A correlation matrix is computed and displayed to understand the interdependencies between variables.

- **Model Preparation and Prediction**:
  - Data is split into training and testing sets.
  - Features are scaled using `StandardScaler`.
  - A logistic regression model is trained and used to make predictions.
  - Model's accuracy is evaluated.

## Requirements

- Python 3
- Libraries: pandas, seaborn, matplotlib, scikit-learn

## Setup and Run

Output:
The script will output:

Box plots for visual exploratory data analysis.
A correlation matrix heatmap to visualize the correlations.
Accuracy of the logistic regression model after prediction.
Additional Notes:
Ensure that the dataset path is correctly set and that the dataset is properly formatted as expected by the script

1. Ensure the file path in the script is updated to your local dataset path.
2. Install necessary Python libraries if not already installed:
   ```bash
   pip install pandas seaborn matplotlib scikit-learn
