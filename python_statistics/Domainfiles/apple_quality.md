# Apple Quality Prediction Analysis

This Python script is designed to perform a comprehensive analysis of apple quality from a dataset. The script handles data cleaning, exploratory data analysis (EDA), and prediction using logistic regression.

## Script Functionality

1. **Data Loading**:
   - Loads data from `apple_quality.csv` (adjust the `file_path` as necessary).

2. **Initial Data Inspection**:
   - Displays the first few rows of the dataset.
   - Provides dataset structure and summary statistics.

3. **Data Preprocessing**:
   - Fills missing values with mean for numeric columns and mode for categorical columns.
   - Converts categorical columns to numeric using one-hot encoding.
   - Removes duplicates.
   - Standardizes column names.

4. **Outlier Detection**:
   - Applies Z-score method to identify and report outliers in numeric columns.

5. **Exploratory Data Analysis (EDA)**:
   - Generates histograms for each numerical column to analyze distributions.
   - Creates box plots to visualize potential outliers in each numeric column.
   - Displays a correlation heatmap to examine relationships between features.

6. **Predictive Modeling - Logistic Regression**:
   - Prepares features and labels, excluding identifiers and target column for prediction.
   - Splits data into training and testing sets.
   - Trains a logistic regression model.
   - Predicts and evaluates model performance with accuracy score and classification report.
   - Visualizes the confusion matrix to assess model predictions.

## Requirements

- Python 3
- Libraries: pandas, numpy, seaborn, matplotlib, scikit-learn

## Usage

- Ensure the CSV file path is correctly set in the script.
- Run the script in a Python environment to process the data and view predictions.

## Outputs

- The script will output various plots to aid in understanding the data and the effectiveness of the logistic regression model.

## Concluding Note

This script provides a thorough analysis of apple quality, using logistic regression to predict quality based on various features. Adjustments to the dataset path and specific analysis requirements may be necessary based on user environment and data specifics.
