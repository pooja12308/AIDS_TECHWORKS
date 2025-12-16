import os
import pandas as pd

def extract_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data", "raw")
    os.makedirs(data_dir, exist_ok=True)

    # 👇 Your original Telco dataset path
    input_path = os.path.join(base_dir, "Telco-Customer-Churn.csv")

    df = pd.read_csv(input_path)

    # Save into raw folder
    raw_path = os.path.join(data_dir, "Telco-Customer-Churn.csv")
    df.to_csv(raw_path, index=False)

    print(f"✅ Data extracted and saved at: {raw_path}")
    return raw_path

if __name__ == "__main__":
    extract_data()
