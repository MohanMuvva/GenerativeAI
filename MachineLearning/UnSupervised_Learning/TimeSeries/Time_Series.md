# Timeseries Analysis

## Script Functionality
This script performs time series analysis on a dataset of Apple (AAPL) stock prices. The primary functions include:
1. **Data Preparation**: Loading and preprocessing the time series data, including splitting date components (year, month, day).
2. **Decomposition of Time Series**: For each year, it decomposes the selected column (e.g., closing price) into trend, seasonality, and residual components using an additive model.
3. **Visualization**: Plots the decomposed components for each year to help visualize patterns in the time series data.

## Requirements
- **Python Libraries**:
  - `pandas`: For data manipulation and loading.
  - `matplotlib.pyplot`: For plotting the time series decomposition.
  - `statsmodels`: For the seasonal decomposition of time series.

Install these libraries using:
```bash
pip install pandas matplotlib statsmodels
##Usage
Place the data file (e.g., AAPL.csv) in the same directory as this script.
##Run the script:
python Timeseriesanalysis.py
The script will load the dataset, preprocess it, and display decomposed components for each year's time series.
##Outputs
Decomposed Time Series Plots: For each year in the dataset, the script produces plots showing:
Trend: Underlying trend component of the selected column.
Seasonality: Repeating patterns within each year.
Residuals: Remaining noise after removing trend and seasonality.
##Concluding Note
This script provides an effective means to understand patterns in stock prices over time by decomposing the series into trend, seasonality, and residuals. It is especially useful for time series data analysis and financial forecasting.