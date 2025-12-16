# ===========================
# transform.py
# ===========================

import os
import pandas as pd

# Purpose: Clean and transform Telco Customer Churn dataset
def transform_data(raw_path):
    # Ensure the path is relative to project root
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # go up one level
    staged_dir = os.path.join(base_dir, "data", "staged")
    os.makedirs(staged_dir, exist_ok=True)

    df = pd.read_csv(raw_path)

    # ===========================
    # 1️⃣ BASIC CLEANING
    # ===========================

    # Remove spaces in column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Convert TotalCharges to numeric
    if "totalcharges" in df.columns:
        df["totalcharges"] = pd.to_numeric(df["totalcharges"], errors="coerce")

    # Fill numeric missing values
    num_cols = df.select_dtypes(include=["int64", "float64"]).columns
    for col in num_cols:
        df[col] = df[col].fillna(df[col].median())

    # Fill categorical missing values
    cat_cols = df.select_dtypes(include=["object"]).columns
    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    # ===========================
    # 2️⃣ FEATURE ENGINEERING
    # ===========================

    # Create tenure groups
    df["tenure_group"] = pd.cut(
        df["tenure"],
        bins=[0, 12, 24, 48, 72],
        labels=["0-12", "12-24", "24-48", "48-72"],
        include_lowest=True
    )

    # Monthly Charges Category
    df["monthlycharges_group"] = pd.cut(
        df["monthlycharges"],
        bins=[0, 35, 70, 120],
        labels=["Low", "Medium", "High"],
        include_lowest=True
    )

    # Total Services Count
    service_cols = [
        "phone_service", "internet_service", "online_security", "online_backup",
        "device_protection", "tech_support", "streaming_tv", "streaming_movies"
    ]
    available_services = [col for col in service_cols if col in df.columns]
    df["total_services"] = df[available_services].apply(
        lambda row: sum(row == "Yes"), axis=1
    )

    # Encode churn as 0/1
    if "churn" in df.columns:
        df["churn"] = df["churn"].replace({"Yes": 1, "No": 0})

    # ===========================
    # 3️⃣ DROP UNNECESSARY COLUMNS
    # ===========================
    drop_cols = ["customerid"]  # keep only if exists
    df.drop(columns=[c for c in drop_cols if c in df.columns], inplace=True)

    # ===========================
    # 4️⃣ SAVE TRANSFORMED DATA
    # ===========================
    staged_path = os.path.join(staged_dir, "telco_transformed.csv")
    df.to_csv(staged_path, index=False)

    print(f"✅ Data transformed and saved at: {staged_path}")
    return staged_path


if __name__ == "__main__":
    from extract import extract_data
    raw_path = extract_data()
    transform_data(raw_path)
