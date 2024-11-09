# Industrial Policy Data Analysis

This Python script analyzes industrial data to assess investment trends and production outputs across various industries.

## Script Functionality
- **Data Loading**: Loads industrial policy dataset from a CSV file.
- **Data Cleaning**:
  - Checks and cleans the 'Industry' column by removing leading and trailing spaces.
  - Handles null values in relevant columns.
- **Data Aggregation**:
  - Groups data by industry to calculate the average investment and production output.
- **Data Visualization**:
  - Generates bar plots to visualize the average investment and production output by industry.
  - Creates box plots to explore the distribution of production output across industries.

## Requirements
- **Programming Language**: Python 3
- **Libraries**:
  ```bash
  pip install pandas seaborn matplotlib

##Usage
Set File Path: Update the file_path variable to point to your dataset location.

##Outputs
Console Outputs: Displays initial data checks and aggregated statistical results.

##Visualizations:
Bar plots for average investment and production outputs by industry.
Box plots for the distribution of production outputs, providing insights into variance and outliers.
Concluding Note
The script offers a foundational analysis for policymakers and industry analysts to evaluate the efficiency and impact of industrial investments and outputs, facilitating data-driven decision making.

##Additional Features
Interactivity: Could be extended to include interactive web-based visualizations using libraries like Plotly or Dash.
Automation: The script can be scheduled to run periodically as new data becomes available, ensuring up-to-date analysis.
Contributing
Contributors are welcome to enhance the script's functionality or documentation. Please fork the repository, make your changes, and submit a pull request.

License
This project is open-sourced under the MIT License. See the LICENSE file for more details.