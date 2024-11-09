# E-Commerce Customer Purchase Prediction

This Python script performs preprocessing and predictive analysis on an e-commerce dataset. The goal is to predict customer purchase behavior based on the dataset provided.

## Features of the Script

- **Data Preprocessing**:
  - Handles missing values and checks for nulls.
  - Encodes categorical variables using Label Encoding.
  - Converts object data types to numeric where applicable.

- **Exploratory Data Analysis (EDA)**:
  - Generates histograms for numerical features.
  - Produces a correlation heatmap to examine feature relationships.
  - Displays count plots for categorical variables to visualize data distributions.

- **Model Preparation and Prediction**:
  - Splits the dataset into training and testing sets.
  - Trains a Logistic Regression model.
  - Makes predictions and evaluates them using accuracy, a confusion matrix, and a classification report.

Usage:

Update the file_path in the script to your local dataset path.
Run the script to process the data, perform the analysis, and output predictions.
Outputs:

Histograms and count plots for a visual understanding of the data.
A correlation matrix to explore potential feature dependencies.
Logistic regression model evaluation results including accuracy and a detailed classification report.
Contributing:

Feel free to fork this repository, make improvements, and submit pull requests.

License
This project is released under the MIT License.

## Installation Requirements

Make sure you have Python and the following packages installed:
- pandas
- matplotlib
- seaborn
- scikit-learn

Install these using pip if they are not already installed:
```bash
pip install pandas matplotlib seaborn scikit-learn

