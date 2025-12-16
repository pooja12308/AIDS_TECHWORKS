#cleaning the dataset loan_approved.csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv('loan_approved.csv')
print("Shape:", df.shape)
print("\nData Types:")
print(df.dtypes)
nominal = []
ordinal = []
discrete = []
continuous = []
for col in df.columns:
    if df[col].dtype == 'object':
        nominal.append(col)
    elif df[col].dtype in ['int64', 'float64']:
        if col in ['Dependents', 'Credit_History', 'Loan_Amount_Term']:
            discrete.append(col)
            ordinal.append(col)   
        elif col in ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']:
            continuous.append(col)
        else:
            continuous.append(col)
print("\nNominal Attributes:", nominal)
print("Ordinal Attributes:", ordinal)
print("Discrete Attributes:", discrete)
print("Continuous Attributes:", continuous)
print(df.isnull())
print(df.isnull().sum())
cat_cols = df.select_dtypes(include='object').columns.tolist()
print("\nCategorical Columns:", cat_cols)
for col in cat_cols:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].mode()[0])
num_cols = df.select_dtypes(include=['int64','float64']).columns.tolist()
print("\nNumerical Columns:", num_cols)
for col in num_cols:
    if df[col].isnull().sum() > 0:
        if col == 'Credit_History':
            df[col] = df[col].fillna(df[col].mode()[0])
        else:
            df[col] = df[col].fillna(df[col].median())
print("\nMissing Values After Cleaning:\n")
print(df.isnull().sum())
# Print full column
print("Loan_Amount_Term Column Values:")
print(df['Loan_Amount_Term'].head())
print()
# Print unique values