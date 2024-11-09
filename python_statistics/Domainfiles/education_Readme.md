# Student Performance Analysis

This Python script is designed for statistical analysis and predictive modeling on student performance data. It explores the impact of various factors on students' GPA.

## Introduction
`education.py` processes a dataset containing information about students' study habits, attendance, and academic performance. It provides statistical summaries, detects outliers, and utilizes machine learning to predict GPA based on selected features.

## Features
- **Data Loading and Cleaning**: Loads data from a CSV file, checks for null values, and handles duplicates.
- **Statistical Analysis**: Computes descriptive statistics including mean, median, mode, standard deviation, min, and max for key variables like GPA.
- **Outlier Detection**: Identifies outliers using a standard deviation method.
- **Exploratory Data Analysis (EDA)**:
  - Generates a correlation heatmap to understand relationships between variables.
  - Creates scatter plots to visualize the relationship between GPA and other factors such as study time and absences.
- **Predictive Modeling**:
  - Uses Linear Regression to model and predict GPA based on variables like study time and absences.
  - Evaluates model performance using Mean Squared Error (MSE) and R² score.

##Usage
Update File Path: Change the file_path variable to the location of your dataset.
Run the Script: Execute the script in your Python environment to perform the analysis.

##Output
Prints descriptive statistics and outlier information.
Displays visualizations including heatmaps and scatter plots.
Outputs model evaluation metrics and a plot comparing actual vs. predicted GPA.

##Contributing
Contributions to improve the script are welcome. Please fork the repository, make your changes, and submit a pull request.


## Installation Requirements
Ensure you have Python installed along with the following libraries:
```bash
pip install pandas seaborn matplotlib scikit-learn

##License
This project is released under the MIT License.

