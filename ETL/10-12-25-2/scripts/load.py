import pandas as pd
from supabase import create_client, Client

# -----------------------------
# Supabase client setup
# -----------------------------
SUPABASE_URL = "https://czvfnptvrmdsenmlwmiw.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN6dmZucHR2cm1kc2VubWx3bWl3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjUzMzgzNjAsImV4cCI6MjA4MDkxNDM2MH0.7jwLgmk1xZADf9v0i9WxMQTiReQApSveL7NHZuzPTIM"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# -----------------------------
# Config
# -----------------------------
staged_csv_path = r"C:\Users\Nihal - Pooju\Desktop\AIDS_TECHWORKS\ETL\10-12-25-2\data\staged\telco_transformed.csv"
table_name = "telco_data"

# -----------------------------
# Helper: create missing columns
# -----------------------------
def ensure_columns_exist(df, table_name):
    # Get current table columns from Supabase
    result = supabase.table(table_name).select("*").limit(1).execute()
    existing_columns = []
    if result.data:
        existing_columns = list(result.data[0].keys())
    
    # Find missing columns in table
    missing_columns = [col for col in df.columns if col not in existing_columns]
    
    # Add missing columns dynamically
    for col in missing_columns:
        # Infer type from dataframe
        dtype = df[col].dtype
        if pd.api.types.is_integer_dtype(dtype):
            sql_type = "BIGINT"
        elif pd.api.types.is_float_dtype(dtype):
            sql_type = "DOUBLE PRECISION"
        elif pd.api.types.is_bool_dtype(dtype):
            sql_type = "BOOLEAN"
        else:
            sql_type = "TEXT"
        
        # Note: execute_sql RPC must exist in your Supabase database
        sql = f'ALTER TABLE {table_name} ADD COLUMN IF NOT EXISTS "{col}" {sql_type};'
        response = supabase.rpc("execute_sql", {"query": sql}).execute()
        if "error" in response and response["error"]:
            print(f"Error adding column {col}: {response['error']}")
        else:
            print(f"Added missing column: {col} ({sql_type})")

# -----------------------------
# Main loader
# -----------------------------
def load_to_supabase(csv_path):
    df = pd.read_csv(csv_path)
    
    # Ensure table exists (Supabase auto-creates if table exists)
    supabase.table(table_name).select("*").limit(1).execute()
    
    # Ensure all CSV columns exist in table
    ensure_columns_exist(df, table_name)
    
    # Load data in batches
    batch_size = 500
    for start in range(0, len(df), batch_size):
        end = start + batch_size
        records = df.iloc[start:end].to_dict(orient="records")
        
        response = supabase.table(table_name).insert(records).execute()
        
        if "error" in response and response["error"]:
            print("Error uploading data:", response["error"])
        else:
            print(f"Batch {start // batch_size + 1} inserted successfully.")

# -----------------------------
# Run loader
# -----------------------------
if __name__ == "__main__":
    load_to_supabase(staged_csv_path)