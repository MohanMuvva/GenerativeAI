
# Traffic Volume Analysis

This Python script analyzes interstate traffic volume data with environmental and temporal variables to understand patterns and predict traffic levels.

## Script Functionality
- **Data Preprocessing**: Handles missing values, converts temperature from Kelvin to Celsius, and applies Label Encoding to categorical variables.
- **Exploratory Data Analysis (EDA)**:
  - Visualizes data distributions and relationships using pair plots and histograms.
  - Removes outliers in temperature and rainfall data using statistical methods.
- **Predictive Modeling**:
  - Employs Linear Regression to forecast traffic volume based on weather conditions and other variables.
  - Validates the model's accuracy and performance with Mean Squared Error and R² Score.

##Usage
Prepare your data:
Ensure the CSV file path is correctly updated in the script.
##Run the Script:

python traffic.py
##Outputs
Visual Outputs: Pair plots, histograms, and scatter plots for comprehensive visual analysis.
Model Evaluation: Displays the MSE and R² Score, and plots Actual vs Predicted Traffic Volume.
##Concluding Note
The analysis aids in understanding how environmental factors like weather impact traffic volumes, providing insights for urban planning and infrastructure development.

License
This project is open-sourced under the MIT License.
## Requirements
- **Python Libraries**: pandas, matplotlib, seaborn, scikit-learn
  ```bash
  pip install pandas matplotlib seaborn scikit-learn
