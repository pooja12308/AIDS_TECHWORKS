#!/usr/bin/env python3
"""
etl_analysis.py

- Read air_quality_data from Supabase
- Compute KPIs:
    * City with highest avg PM2.5
    * City with highest avg severity_score
    * % of High/Moderate/Low risk hours
    * Hour of day with worst AQI (PM2.5)
- City pollution trends
- Export CSVs to data/processed/
- Save visualizations to data/processed/
"""

import os
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

client = create_client(SUPABASE_URL, SUPABASE_KEY)

PROCESSED_DIR = "data/processed"
os.makedirs(PROCESSED_DIR, exist_ok=True)

# ---------------- Load data ----------------
print("📥 Fetching data from Supabase...")
res = client.table("air_quality_data").select("*").execute()
records = res.data

if not records:
    print("⚠ No data found in Supabase table!")
    exit()

df = pd.DataFrame(records)

# Convert numeric columns
numeric_cols = [
    "pm10", "pm2_5", "carbon_monoxide", "nitrogen_dioxide",
    "sulphur_dioxide", "ozone", "uv_index", "severity_score", "hour"
]
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Convert time to datetime
df["time"] = pd.to_datetime(df["time"], errors="coerce")

# ---------------- KPI Metrics ----------------
print("📊 Computing KPIs...")

# City with highest average PM2.5
city_pm25 = df.groupby("city")["pm2_5"].mean().idxmax()
avg_pm25 = df.groupby("city")["pm2_5"].mean().max()

# City with highest average severity score
city_severity = df.groupby("city")["severity_score"].mean().idxmax()
avg_severity = df.groupby("city")["severity_score"].mean().max()

# % of High/Moderate/Low risk hours
risk_counts = df["risk_flag"].value_counts(normalize=True) * 100

# Hour of day with worst avg PM2.5
hour_worst_pm25 = df.groupby("hour")["pm2_5"].mean().idxmax()

# Save summary metrics
summary_metrics = pd.DataFrame({
    "metric": [
        "City with highest avg PM2.5",
        "Average PM2.5",
        "City with highest avg severity",
        "Average severity",
        "Hour with worst PM2.5"
    ],
    "value": [
        city_pm25,
        round(avg_pm25,2),
        city_severity,
        round(avg_severity,2),
        hour_worst_pm25
    ]
})
summary_metrics.to_csv(f"{PROCESSED_DIR}/summary_metrics.csv", index=False)
print("✅ Saved summary_metrics.csv")

# ---------------- City Risk Distribution ----------------
city_risk = df.groupby(["city", "risk_flag"]).size().reset_index(name="count")
city_risk_pivot = city_risk.pivot(index="city", columns="risk_flag", values="count").fillna(0)
city_risk_pivot.to_csv(f"{PROCESSED_DIR}/city_risk_distribution.csv")
print("✅ Saved city_risk_distribution.csv")

# ---------------- Pollution Trends ----------------
trends_cols = ["time", "city", "pm2_5", "pm10", "ozone"]
df[trends_cols].to_csv(f"{PROCESSED_DIR}/pollution_trends.csv", index=False)
print("✅ Saved pollution_trends.csv")

# ---------------- Visualizations ----------------
sns.set(style="whitegrid")

# Histogram of PM2.5
plt.figure(figsize=(8,6))
sns.histplot(df["pm2_5"].dropna(), bins=30, kde=True)
plt.title("Histogram of PM2.5")
plt.xlabel("PM2.5")
plt.ylabel("Frequency")
plt.savefig(f"{PROCESSED_DIR}/hist_pm25.png")
plt.close()
print("✅ Saved hist_pm25.png")

# Bar chart of risk flags per city
plt.figure(figsize=(8,6))
city_risk_plot = city_risk_pivot.plot(kind="bar", stacked=True)
plt.title("Risk Flags per City")
plt.xlabel("City")
plt.ylabel("Number of Hours")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{PROCESSED_DIR}/bar_risk_flags.png")
plt.close()
print("✅ Saved bar_risk_flags.png")

# Line chart of hourly PM2.5 trends per city
plt.figure(figsize=(10,6))
for city in df["city"].unique():
    city_data = df[df["city"] == city].sort_values("time")
    plt.plot(city_data["time"], city_data["pm2_5"], label=city)
plt.title("Hourly PM2.5 Trends per City")
plt.xlabel("Time")
plt.ylabel("PM2.5")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f"{PROCESSED_DIR}/line_pm25_trends.png")
plt.close()
print("✅ Saved line_pm25_trends.png")

# Scatter: severity_score vs pm2_5
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="pm2_5", y="severity_score", hue="city")
plt.title("Severity Score vs PM2.5")
plt.xlabel("PM2.5")
plt.ylabel("Severity Score")
plt.legend()
plt.tight_layout()
plt.savefig(f"{PROCESSED_DIR}/scatter_severity_pm25.png")
plt.close()
print("✅ Saved scatter_severity_pm25.png")
print("🎉 ETL Analysis Completed!")
