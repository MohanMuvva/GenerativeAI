# Health Insurance Cost Prediction

This Python script analyzes health insurance data to predict costs based on various factors such as age, BMI, smoking status, and number of children. It employs linear regression to make these predictions and provides detailed statistical insights and visualizations of the data.

## Introduction
`health_insurance.py` processes insurance dataset information to predict expenses using linear regression. It includes comprehensive data cleaning, outlier detection, and exploratory data analysis (EDA).

## Features
- **Data Loading**: Loads the dataset from a specified CSV file.
- **Data Cleaning**:
  - Checks for null values and handles missing data.
  - Identifies and removes outliers using the Interquartile Range (IQR) method.
  - Converts categorical variables to numerical values using Label Encoding.
- **Exploratory Data Analysis (EDA)**:
  - Generates correlation heatmaps to examine interdependencies between variables.
  - Produces scatter plots and boxplots to explore relationships between features and insurance expenses.
- **Predictive Modeling**:
  - Splits the data into training and testing sets.
  - Trains a Linear Regression model.
  - Evaluates the model's performance using Mean Squared Error (MSE) and R² score.
  - Visualizes actual vs. predicted expenses.

## Output 
	Outputs include statistical summaries, identification of outliers, and visualizations such as heatmaps and scatter plots.
	The script will display a plot of actual versus predicted insurance expenses to evaluate the model accuracy

##Contributing
Contributions to enhance the script are encouraged. Please ensure you update tests as appropriate and provide a clear pull request description.

##License
This project is licensed under the MIT License - see the LICENSE file for details.




## Installation Requirements
Ensure you have Python installed along with the following packages:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
