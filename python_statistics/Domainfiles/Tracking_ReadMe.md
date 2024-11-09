# Daily Activity Data Analysis

This Python script analyzes daily activity data to explore relationships between various physical activities and caloric output, employing statistical and machine learning techniques.

## Script Functionality
- **Data Cleaning**: Identifies and cleans null values, converts categorical variables to numerical ones using Label Encoding.
- **Outlier Detection**: Implements outlier detection and replacement for physical activity distances.
- **Data Visualization**:
  - Generates a correlation heatmap to identify relationships between features.
  - Produces box plots for key variables to visualize data spread and outliers.
- **Predictive Modeling**:
  - Uses Linear Regression to predict calorie output based on activity levels.
  - Evaluates the model using Mean Squared Error (MSE) and R² Score.
##Usage
Set up your dataset:
Update the file_path to the location of your dataset.
##Execute the Script:
python Tracking.py
##Outputs
Descriptive Statistics: Statistical summary of the dataset.
Visual Analysis: Heatmaps and box plots for exploratory analysis.
Model Performance: Outputs the MSE and R² Score of the regression model.
##Concluding Note
The script is designed to facilitate an understanding of how different activity levels influence caloric expenditure, useful for health and fitness analytics.

##License
This project is licensed under the MIT License.

## Requirements
- **Python Libraries**: pandas, seaborn, matplotlib, scikit-learn
  ```bash
  pip install pandas seaborn matplotlib scikit-learn
