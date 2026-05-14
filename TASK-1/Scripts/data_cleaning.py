import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv(r"C:\Users\DEEPIKA\OneDrive\apex\Data Set\Sample - Superstore.csv", encoding='latin1')

# Basic information
print("Dataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)

# Convert date columns
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

print("\nUpdated Data Types:")
print(df.dtypes)

# Numerical columns
numerical_cols = ['Sales', 'Quantity', 'Discount', 'Profit']

print("\nSummary Statistics:")
print(df[numerical_cols].describe())

# Create new features
df['Order Year'] = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month
df['Shipping Days'] = (df['Ship Date'] - df['Order Date']).dt.days

print("\nFeature Engineering Completed")
print(df[['Order Year', 'Order Month', 'Shipping Days']].head())

# Save cleaned dataset
#df.to_csv("../scripts/cleaned_superstore_data.csv", index=False)

#print("\nCleaned dataset saved successfully!")

# Missing values report
missing_report = df.isnull().sum()
missing_report.to_csv("../scripts/missing_values_report.csv")

# Outlier summary report
outlier_summary = df[['Sales', 'Profit']].describe()
outlier_summary.to_csv("../scripts/outlier_summary.csv")

print("\nReports generated successfully!")