#!/usr/bin/env python3
import os, time, json, logging
from pathlib import Path
import requests, pandas as pd
from supabase import create_client
from dotenv import load_dotenv
import matplotlib.pyplot as plt, seaborn as sns

load_dotenv()
BASE = Path(__file__).parent
RAW, STAGED, PROC = [BASE / d for d in ["data/raw","data/staged","data/processed"]]
for d in [RAW, STAGED, PROC]: d.mkdir(exist_ok=True, parents=True)

CITIES = ["Delhi","Bengaluru","Hyderabad","Mumbai","Kolkata"]
POLLUTANTS = ["pm10","pm2_5","carbon_monoxide","nitrogen_dioxide","sulphur_dioxide","ozone","uv_index"]

SUP_URL, SUP_KEY, TABLE = os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"), "air_quality_data"
client = create_client(SUP_URL, SUP_KEY)

logging.basicConfig(level=logging.INFO); log = logging.getLogger()

# ------------- Extract -------------
def extract_city(city):
    LATLON={"Delhi":(28.6139,77.2090),"Bengaluru":(12.9716,77.5946),"Hyderabad":(17.385,78.4867),
            "Mumbai":(19.076,72.8777),"Kolkata":(22.5726,88.3639)}
    url="https://air-quality-api.open-meteo.com/v1/air-quality"
    for _ in range(3):
        try:
            r=requests.get(url,params={"latitude":LATLON[city][0],"longitude":LATLON[city][1],"hourly":",".join(POLLUTANTS)},timeout=30)
            r.raise_for_status(); data=r.json()
            if not data: raise ValueError("Empty")
            path = RAW/f"{city.lower()}.json"
            path.write_text(json.dumps(data)); log.info(f"Saved {city}")
            return path
        except Exception as e: log.warning(f"{city} extract failed: {e}"); time.sleep(2)
    return None

def extract_all(): return [extract_city(c) for c in CITIES]

# ------------- Transform -------------
def flatten(path):
    j=json.load(open(path)); h=j.get("hourly",{}); t=h.get("time",[])
    if not t: return pd.DataFrame()
    df=pd.DataFrame({p:h.get(p,[None]*len(t)) for p in POLLUTANTS})
    df["time"]=pd.to_datetime(t,utc=True); df["city"]=path.stem.split(".")[0].capitalize()
    return df[["city","time"]+POLLUTANTS]

def aqi(pm): return None if pd.isna(pm) else "Good" if pm<=50 else "Moderate" if pm<=100 else "Unhealthy" if pm<=200 else "Very Unhealthy" if pm<=300 else "Hazardous"
def severity(row): return sum((row.get(p) or 0)*w for p,w in zip(POLLUTANTS,[3,5,2,4,4,3,1]))
def risk(sev): return "High Risk" if sev>400 else "Moderate Risk" if sev>200 else "Low Risk"

def transform_all():
    dfs=[flatten(f) for f in RAW.glob("*.json")]; dfs=[d for d in dfs if not d.empty]
    if not dfs: return pd.DataFrame()
    df=pd.concat(dfs,ignore_index=True); df=df[~df[POLLUTANTS].isna().all(axis=1)]
    df["aqi_category"]=df["pm2_5"].apply(aqi)
    df["severity_score"]=df.apply(severity,axis=1)
    df["risk_flag"]=df["severity_score"].apply(risk)
    df["hour"]=df["time"].dt.hour; df.to_csv(STAGED/"air_quality_transformed.csv",index=False)
    return df

# ------------- Load -------------
def load(df):
    for start in range(0,len(df),200):
        batch=df.iloc[start:start+200].where(pd.notnull(df),None).to_dict("records")
        for _ in range(2):
            try: client.table(TABLE).insert(batch).execute(); break
            except: time.sleep(2)

# ------------- Analysis -------------
def analyze(df):
    df.to_csv(PROC/"air_quality_final.csv",index=False)
    pd.DataFrame([{"city_highest_pm25":df.groupby("city")["pm2_5"].mean().idxmax(),
                   "city_highest_severity":df.groupby("city")["severity_score"].mean().idxmax()}]).to_csv(PROC/"summary_metrics.csv",index=False)
    df.groupby(["city","risk_flag"]).size().unstack(fill_value=0).to_csv(PROC/"city_risk_distribution.csv")
    df[["city","time","pm2_5","pm10","ozone"]].to_csv(PROC/"pollution_trends.csv",index=False)
    sns.histplot(df["pm2_5"].dropna()); plt.savefig(PROC/"pm25_hist.png"); plt.clf()
    df.groupby("city")["risk_flag"].value_counts().unstack().plot(kind="bar"); plt.savefig(PROC/"risk_bar.png"); plt.clf()
    for c in df["city"].unique(): plt.plot(df[df["city"]==c]["time"],df[df["city"]==c]["pm2_5"],label=c)
    plt.legend(); plt.savefig(PROC/"pm25_trends.png"); plt.clf()
    plt.scatter(df["pm2_5"],df["severity_score"]); plt.savefig(PROC/"severity_scatter.png"); plt.clf()

# ------------- Main -------------
def main():
    print("🚀 Running ETL Pipeline")
    extract_all(); df=transform_all()
    if df.empty: print("⚠ No data to load"); return
    load(df); print("✅ Load complete")
    analyze(df); print("✅ Analysis complete")

if __name__=="__main__": main()
