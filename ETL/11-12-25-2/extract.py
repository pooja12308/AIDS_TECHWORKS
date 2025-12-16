''' Urban Air Quality Monitoring – Multi-City ETL Pipeline
A government environmental agency wants to build an automated analytics system that monitors air quality across multiple Indian cities. The agency provides an open, unauthenticated API (no token required) that returns Air Quality Index (AQI) and pollutant information.
You are required to build a complete ETL pipeline (Extract → Transform → Load → Analyze) using Python and Supabase.
🟦 1️⃣ Extract (extract.py)
Use the following public API:
API Endpoint (No Token Needed):
OpenAQ API (Public Open Data):
https://api.openaq.org/v2/latest
Your task
Write code that:
Fetches AQI readings for 5 cities:
Delhi, Bengaluru, Hyderabad, Mumbai, Kolkata
For each city, call the API with a query like:
Save each API response separately inside:
Implement:
Retry logic (3 attempts)
Graceful failure handling
Logging of errors and empty responses
Return list of all saved file paths.'''


import json
import logging
from datetime import datetime
from pathlib import Path
import requests
import time

BASE_DIR = Path(__file__).resolve().parents[0]
RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

CITIES = ["Delhi", "Bengaluru", "Hyderabad", "Mumbai", "Kolkata"]

URL = "https://air-quality-api.open-meteo.com/v1/air-quality?latitude=17.3850&longitude=78.4867&hourly=pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,ozone,sulphur_dioxide"

MAX_RETRIES = 3
SLEEP_BETWEEN_RETRIES = 2  # seconds

# ---------------- LOGGING ------------------
LOG_FILE = BASE_DIR / "extract.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger()


def save_json(city: str, data: dict, type_tag="normal") -> Path:
    """Save JSON with timestamp and return path."""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = RAW_DIR / f"{city.lower()}{type_tag}{timestamp}.json"
    filename.write_text(json.dumps(data, indent=2))
    return filename


def extract_aqi_data(city: str):
    """
    Fetch AQI data for a given city with:
    - Retry logic (3 attempts)
    - Graceful failure handling
    - Logging
    """
    print(f"⏳ Requesting AQI data for city={city} ...")

    attempts = 0
    last_error = None

    while attempts < MAX_RETRIES:
        attempts += 1
        try:
            resp = requests.get(URL, timeout=30)
            resp.raise_for_status()
            data = resp.json()

            # Check for empty response
            if not data:
                logger.warning(f"Empty response for city={city}")
                fallback = {"city": city, "error": "Empty API response"}
                saved_path = save_json(city, fallback, type_tag="empty")
                return saved_path

            saved_path = save_json(city, data)
            print(f"✅ Saved AQI data for {city} → {saved_path}")
            logger.info(f"Success: {city} saved to {saved_path}")
            return saved_path

        except Exception as e:
            last_error = str(e)
            logger.error(f"Attempt {attempts} failed for city={city} → {e}")
            print(f"⚠ Attempt {attempts}/{MAX_RETRIES} failed for {city}: {e}")

            if attempts < MAX_RETRIES:
                print(f"⏳ Retrying in {SLEEP_BETWEEN_RETRIES} seconds...\n")
                time.sleep(SLEEP_BETWEEN_RETRIES)

    # After 3 failed attempts → save fallback error file
    print(f"❌ Failed to fetch AQI for {city} after {MAX_RETRIES} attempts.")
    fallback_data = {"city": city, "error": last_error}
    error_path = save_json(city, fallback_data, type_tag="error")
    logger.error(f"FAILED {city} → Error saved to {error_path}")
    return error_path


def extract_all_cities():
    saved_files = []
    for city in CITIES:
        path = extract_aqi_data(city)
        saved_files.append(str(path))

    print("🎉 AQI extraction completed!")
    print("Saved files:")
    for file in saved_files:
        print(" -", file)

    return saved_files


if __name__ == "__main__":
    extract_all_cities()