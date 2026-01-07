import os
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Telco Customer Churn Predictor",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Telco Customer Churn Prediction")
st.markdown(
    "Predict whether a customer is **likely to churn** using a Logistic Regression model."
)

st.divider()

# ---------------------------------------------------
# LOAD DATA (ROBUST)
# ---------------------------------------------------
@st.cache_data
def load_data():
    file_path = "Telcom_Customer_Churn.csv"

    if not os.path.exists(file_path):
        st.error("❌ Dataset file not found!")
        st.info(
            "Please upload **Telcom_Customer_Churn.csv** to the same folder "
            "as this app.py file in your GitHub repository."
        )
        st.stop()

    return pd.read_csv(file_path)

df = load_data()

# ---------------------------------------------------
# FEATURE SELECTION
# ---------------------------------------------------
X = df[['tenure', 'MonthlyCharges', 'TotalCharges']]
y = df['Churn']

# ---------------------------------------------------
# DATA CLEANING (SAME LOGIC YOU LEARNED)
# ---------------------------------------------------
X['TotalCharges'] = pd.to_numeric(X['TotalCharges'], errors='coerce')
X = X.dropna()
y = y.loc[X.index]
y = y.map({'Yes': 1, 'No': 0})

# ---------------------------------------------------
# TRAIN-TEST SPLIT
# ---------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------------------------------------------
# FEATURE SCALING
# ---------------------------------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ---------------------------------------------------
# MODEL TRAINING
# ---------------------------------------------------
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# ---------------------------------------------------
# SIDEBAR INPUTS
# ---------------------------------------------------
st.sidebar.header("🧾 Customer Details")

tenure = st.sidebar.slider("Tenure (months)", 0, 72, 12)
monthly_charges = st.sidebar.slider("Monthly Charges ($)", 20.0, 120.0, 70.0)
total_charges = st.sidebar.number_input(
    "Total Charges ($)", min_value=0.0, value=1000.0
)

# ---------------------------------------------------
# PREDICTION
# ---------------------------------------------------
input_data = pd.DataFrame({
    'tenure': [tenure],
    'MonthlyCharges': [monthly_charges],
    'TotalCharges': [total_charges]
})

input_scaled = scaler.transform(input_data)
churn_probability = model.predict_proba(input_scaled)[0][1]
churn_prediction = model.predict(input_scaled)[0]

# ---------------------------------------------------
# OUTPUT
# ---------------------------------------------------
st.divider()
st.subheader("🔍 Prediction Result")

if churn_prediction == 1:
    st.error("❌ Customer is **LIKELY TO CHURN**")
else:
    st.success("✅ Customer is **LIKELY TO STAY**")

st.metric(
    label="Churn Probability",
    value=f"{churn_probability:.2%}"
)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.divider()
st.caption(
    "Model: Logistic Regression | Features: Tenure, Monthly Charges, Total Charges"
)
