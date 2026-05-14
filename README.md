Superstore Sales Analytics & Business Intelligence

Project Overview
This project was developed as part of a Data Analytics internship task focused on understanding and preparing raw business data for analysis. Using the Sample Superstore dataset, I performed data cleaning, transformation, and feature engineering to make the dataset analysis-ready for future business intelligence and visualization tasks.


Objective
The main objective of this project was to:
- Understand the structure of a real-world sales dataset
- Identify and handle data quality issues
- Perform data cleaning and preprocessing
- Create meaningful features from existing data
- Prepare a clean dataset for analytics and dashboard creation



Dataset Information
Dataset Name: Sample Superstore Dataset

Total Records: 9994 rows  
Total Columns: 21 columns

The dataset includes:
- Sales and profit details
- Customer information
- Product categories
- Shipping details
- Regional sales data



Tools & Technologies Used
- Python
- Pandas
- NumPy
- VS Code
- CSV Dataset



Steps Performed

1. Data Loading
Loaded the dataset using the Pandas library in Python.

2. Data Familiarization
- Checked the size of the dataset
- Reviewed column names
- Displayed sample records to understand the data structure

3. Data Quality Assessment
- Checked for missing values
- Checked duplicate rows
- Verified data types of all columns
- Analyzed summary statistics of numerical columns

4. Data Transformation
Converted the `Order Date` and `Ship Date` columns into datetime format for easier analysis.

5. Feature Engineering
Created new columns:
- Order Year
- Order Month
- Shipping Days

These features help in analyzing sales trends and delivery performance.

6. Dataset Export
Saved the cleaned and transformed dataset as a new CSV file for future analysis.



Key Findings
- No missing values were found in the dataset
- No duplicate records were identified
- Some transactions showed negative profit values
- High sales and discount values indicated possible outliers
- Shipping duration was successfully calculated using order and ship dates



Project Outputs
- cleaned_superstore_data.csv
- data_cleaning.py
- missing_values_report.csv
- outlier_summary.csv
- data_dictionary.xlsx



Future Scope
In the future, this project can be extended by:
- Performing Exploratory Data Analysis (EDA)
- Creating Tableau dashboards
- Analyzing KPIs and sales trends
- Building business intelligence reports
- Performing predictive analytics
