# load.py
import pandas as pd
import numpy as np
from supabase import create_client
import os
from dotenv import load_dotenv
import time
import math

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
BATCH_SIZE = 200
MAX_RETRIES = 2

client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Load transformed CSV
df = pd.read_csv("data/staged/air_quality_transformed.csv")

# Rename columns to match DB schema
df = df.rename(
    columns={
        "aqi_pm25": "aqi_category",
        "severity": "severity_score",
        "risk": "risk_flag",
    }
)

# ---------------- JSON-safe numeric conversion ----------------
# Convert NaN → None
df = df.where(pd.notnull(df), None)

# Ensure all numeric columns are finite floats (JSON-compliant)
float_cols = [
    "pm10", "pm2_5", "carbon_monoxide", "nitrogen_dioxide",
    "sulphur_dioxide", "ozone", "uv_index", "severity_score"
]

for col in float_cols:
    if col in df.columns:
        new_vals = []
        for v in df[col]:
            if v is None:
                new_vals.append(None)
            elif isinstance(v, (float, int)):
                if math.isfinite(v):
                    new_vals.append(float(v))
                else:
                    new_vals.append(None)
            else:
                # catch any string or bad type
                new_vals.append(None)
        df[col] = new_vals

# Convert datetime to ISO string
df["time"] = pd.to_datetime(df["time"]).apply(lambda x: x.isoformat() if x else None)

total_rows = len(df)
inserted_rows = 0

print(f"🚀 Starting load to Supabase: {total_rows} rows...")

for start in range(0, total_rows, BATCH_SIZE):
    end = start + BATCH_SIZE
    batch = df.iloc[start:end].to_dict(orient="records")

    attempts = 0
    while attempts <= MAX_RETRIES:
        try:
            res = client.table("air_quality_data").insert(batch).execute()
            inserted_rows += len(batch)
            print(f"✅ Inserted batch {start}-{end} ({len(batch)} rows)")
            break
        except Exception as e:
            attempts += 1
            print(f"⚠ Batch {start}-{end} failed on attempt {attempts}: {e}")
            time.sleep(2)
            if attempts > MAX_RETRIES:
                print(f"❌ Failed to insert batch {start}-{end} after {MAX_RETRIES} retries")

print(f"🎉 Load completed! Total rows attempted: {total_rows}, inserted: {inserted_rows}")
