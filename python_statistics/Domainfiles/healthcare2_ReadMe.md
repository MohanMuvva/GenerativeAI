# Healthcare Data Analysis for Diabetes Prediction

This Python script analyzes healthcare data to predict diabetes outcomes and insulin levels using logistic and linear regression models respectively. It also performs various statistical tests to explore data relationships.

## Script Functionality
- **Data Cleaning**: Removes rows with null values and those where 'SkinThickness' is zero.
- **Exploratory Data Analysis**: Includes correlation heatmaps and visualizations to identify relationships between variables.
- **Predictive Modeling**:
  - **Logistic Regression**: Predicts binary outcomes (diabetes yes/no) based on several predictors.
  - **Linear Regression**: Predicts continuous values (insulin levels) and calculates the margin of error for these predictions.
- **Statistical Testing**:
  - **T-tests and A/B Testing**: Compares mean glucose and insulin levels between groups.
  - **Chi-Square Test**: Tests for independence between 'Outcome' and 'SkinThickness'.
##Usage
Prepare your data: Ensure the dataset is located at the specified path or update the file_path variable.

##Outputs
Visual Outputs: Correlation heatmaps, scatter plots, and regression plots that visually represent data relationships and model predictions.
Statistical Outputs: Console outputs for model evaluations, margin of error calculations, and results from statistical tests.
##Concluding Note
This script is a comprehensive tool for analyzing healthcare data related to diabetes. It provides insights not only through predictive modeling but also through rigorous statistical testing to ensure robust findings.

##Contributing
To contribute to this project, please fork the repository, make your changes, and submit a pull request. Ensure that you update the testing suite and documentation as necessary.

License
This project is licensed under the MIT License. Please refer to the LICENSE file for more details.

## Requirements
- **Programming Language**: Python
- **Libraries**:
  ```bash
  pip install pandas numpy matplotlib seaborn scikit-learn scipy
