

# Titanic Survival Analysis

This Python script analyzes the Titanic dataset to predict survival rates using logistic regression and explores passenger demographics through visualizations and statistical testing.

## Script Functionality
- **Data Cleaning**: Fills missing values and removes outliers.
- **Categorical Encoding**: Transforms categorical variables into numerical values suitable for modeling.
- **Data Visualization**: Generates plots to visualize age distribution by gender and survival rates.
- **K-Means Clustering**: Segments passengers into clusters based on ticket class, age, and fare.
- **Logistic Regression**: Predicts survival based on features like age, gender, class, and fare.
- **Statistical Tests**: Conducts Z-tests to compare means across different passenger groups.
##Usage
Ensure the dataset path is updated, install the required libraries, and execute the script with:
python titanic.py

##Outputs
Descriptive statistics, visualization of distributions, and clustering results.
Model performance metrics including accuracy and a classification report.
##Concluding Note
This script provides a detailed exploration of the Titanic dataset, offering insights into factors affecting survival and predicting outcomes with a machine learning model.

##Contributing
To contribute to this project, please fork the repository, make your suggested changes, and submit a pull request.

##License
The project is available under the MIT License.

## Requirements
- Python 3
- Libraries: pandas, numpy, seaborn, matplotlib, scikit-learn, scipy
  ```bash
  pip install pandas numpy seaborn matplotlib scikit-learn scipy
