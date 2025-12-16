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
print("Unique Values in Loan_Amount_Term:")
print(df['Loan_Amount_Term'].unique())
print()

# Print total number of unique values
print("Total Number of Unique Values:")
print(df['Loan_Amount_Term'].nunique())

# Print first few LoanAmount values
print("LoanAmount Column Values:")
print(df['LoanAmount'].head())
print()

# Print unique values in LoanAmount
print("Unique Values in LoanAmount:")
print(df['LoanAmount'].unique())
print()

# Print total number of unique values
print("Total Number of Unique LoanAmount Values:")
print(df['LoanAmount'].nunique())
print("Mean of Loan_Amount_Term:", df['Loan_Amount_Term'].mean())
print("Median of Loan_Amount_Term:", df['Loan_Amount_Term'].median())

print("Mean of Credit_History:", df['Credit_History'].mean())
print("Median of Credit_History:", df['Credit_History'].median())

s=(df['ApplicantIncome']-df['ApplicantIncome'].mean())/df['ApplicantIncome'].std()
print("Mean of ApplicantIncome:", df['ApplicantIncome'].mean()) 
print(s.max())
#saving the cleaned data
df.to_csv('loan_approved_cleaned.csv', index=False)
df=pd.read_csv('loan_approved.csv')

df['CoapplicantIncome'].kurtosis()
df['CoapplicantIncome'].skew()
sns.histplot(df['CoapplicantIncome'])
from sklearn.preprocessing import PowerTransformer
trans=PowerTransformer(method='yeo-johnson')
la_trans=trans.fit_transform(df[['CoapplicantIncome']])
la_trans.shape
print("Skewness:",pd.Series(la_trans.reshape(614,)).skew())
print("Kurtosis:",pd.Series(la_trans.reshape(614,)).kurtosis())
trans_app=PowerTransformer(method='yeo-johnson')
la_trans_app=trans_app.fit_transform(df[['ApplicantIncome']])
la_trans_app.shape
print("Skewness:",pd.Series(la_trans_app.reshape(614,)).skew())
print("Kurtosis:",pd.Series(la_trans_app.reshape(614,)).kurtosis())
sns.histplot(la_trans_app)