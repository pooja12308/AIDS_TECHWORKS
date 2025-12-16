import pandas as pd
from supabase import create_client, Client
import os

# -----------------------------
# Supabase client setup
# -----------------------------
SUPABASE_URL = "https://czvfnptvrmdsenmlwmiw.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN6dmZucHR2cm1kc2VubWx3bWl3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjUzMzgzNjAsImV4cCI6MjA4MDkxNDM2MH0.7jwLgmk1xZADf9v0i9WxMQTiReQApSveL7NHZuzPTIM"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# -----------------------------
# Paths
# -----------------------------
original_csv_path = r"C:\Users\Nihal - Pooju\Desktop\AIDS_TECHWORKS\ETL\10-12-25-2\data\staged\telco_transformed.csv"
processed_output_path = r"C:\Users\Nihal - Pooju\Desktop\AIDS_TECHWORKS\ETL\10-12-25-2\data\processed\telco_validated.csv"
table_name = "telco_data"

# Create directory if not exists
os.makedirs(os.path.dirname(processed_output_path), exist_ok=True)

# -----------------------------
# Load original dataset
# -----------------------------
df_original = pd.read_csv(original_csv_path)

# -----------------------------
# Load Supabase dataset
# -----------------------------
data = supabase.table(table_name).select("*").execute()
df_supabase = pd.DataFrame(data.data)

# -----------------------------
# Validation checks
# -----------------------------
validation_summary = {}

# 1. Missing value checks
critical_cols = ["tenure", "monthlycharges", "totalcharges"]

for col in critical_cols:
    missing = df_supabase[col].isnull().sum()
    validation_summary[f"{col}_missing"] = missing

# 2. Unique row comparison
validation_summary["unique_rows_match"] = (
    len(df_supabase.drop_duplicates()) == len(df_original.drop_duplicates())
)

# 3. Row count comparison
validation_summary["row_count_match"] = len(df_supabase) == len(df_original)

# 4. Segment validation
segment_cols = ["tenure_group", "monthlycharges_group"]

for col in segment_cols:
    missing_segments = set(df_original[col].unique()) - set(df_supabase[col].unique())
    if len(missing_segments) == 0:
        validation_summary[f"{col}_segments"] = "All segments exist"
    else:
        validation_summary[f"{col}_segments_missing"] = missing_segments

# 5. Contract code validation
valid_contracts = {0, 1, 2}
invalid_codes = set(df_supabase["contract"].unique()) - valid_contracts

if invalid_codes:
    validation_summary["invalid_contract_codes"] = invalid_codes
else:
    validation_summary["invalid_contract_codes"] = "All contract codes valid"

# -----------------------------
# Save validated data to processed folder
# -----------------------------
df_supabase.to_csv(processed_output_path, index=False)

print("\n====== SUPABASE DATA VALIDATION SUMMARY ======")
for k, v in validation_summary.items():
    print(f"{k}: {v}")
print("==============================================")
print(f"\n💾 Validated dataset stored at:\n{processed_output_path}")
