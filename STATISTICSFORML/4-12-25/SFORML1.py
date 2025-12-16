import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Fix spelling mistakes in the data
data = [
    'manager','junior developer','senior developer','senior developer','manager',
    'manager','senior developer','junior developer','manager','senior developer',
    'junior developer','junior developer','junior developer','manager',
    'senior developer','manager','senior developer','junior developer',
    'manager','manager'
]

df = pd.Series(data)
print("Original Data:\n", df)

encoder = LabelEncoder()
encoder_emp = encoder.fit_transform(df)

print("\nEncoded Values:", encoder_emp)
print("Classes Mapping:", encoder.classes_)
print("Unique Encoded Labels:", pd.unique(encoder_emp))
