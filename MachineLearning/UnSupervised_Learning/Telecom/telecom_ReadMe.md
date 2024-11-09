# Telecom Churn Analysis

This Python script analyzes customer churn data for a telecom company to identify key factors influencing churn and predict customer retention.

## Script Functionality
- **Data Preprocessing**: Cleans data by encoding categorical variables and handling missing values.
- **Principal Component Analysis (PCA)**: Reduces dimensionality of the data while retaining 95% variance to simplify the model without losing key information.
- **K-Means Clustering**: Applies clustering to segment customers based on their attributes, aiding in targeted marketing     strategies.
- **Logistic Regression**: Utilizes logistic regression to predict the probability of churn based on customer attributes.
- **Cross-Validation**: Implements K-Fold cross-validation to ensure the model's robustness and generalizability.

##Usage
Update the dataset path in the script, install necessary libraries, and run the script using:

##Outputs
Statistical summaries, PCA component analysis, and cluster visualization.
Predictive accuracy assessment and detailed classification report.
##Concluding Note
The analysis provides insights into customer behavior, supporting strategic decisions to reduce churn and enhance customer engagement.

##Contributing
Contributions for improving the script are welcome. Please fork the repository, make your changes, and submit a pull request.

##License
This project is released under the MIT License.

## Requirements
- Python 3
- Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn
  ```bash
  pip install pandas numpy matplotlib seaborn scikit-learn
