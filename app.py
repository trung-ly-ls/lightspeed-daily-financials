#!/usr/bin/env python3
import os
import json
import time
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

# --- Load environment variables ---
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
BUSINESS_LOCATION_ID = os.getenv("BUSINESS_LOCATION_ID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
INCLUDE_PARAMS = os.getenv("INCLUDE_PARAMS", "payments,consumer")

START_DATE = datetime.strptime(os.getenv("START_DATE", "2025-10-09"), "%Y-%m-%d")
END_DATE = datetime.strptime(os.getenv("END_DATE", "2025-10-21"), "%Y-%m-%d")
SLEEP_SECONDS = float(os.getenv("SLEEP_SECONDS", "1"))

OUTPUT_DIR = "./financials"
os.makedirs(OUTPUT_DIR, exist_ok=True)

headers = {
    "Authorization": f"Bearer {AUTH_TOKEN}",
    "Accept": "application/json"
}

current_date = START_DATE

while current_date <= END_DATE:
    date_str = current_date.strftime("%Y-%m-%d")
    url = f"{BASE_URL}/{BUSINESS_LOCATION_ID}/dailyFinancials?include={INCLUDE_PARAMS}&date={date_str}"

    print(f"Fetching data for {date_str}...")
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        output_file = os.path.join(OUTPUT_DIR, f"dailyFinancials_{date_str}.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"✅ Saved: {output_file}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching {date_str}: {e}")
        with open(os.path.join(OUTPUT_DIR, "error_log.txt"), "a") as log:
            log.write(f"{date_str} - {e}\n")

    current_date += timedelta(days=1)
    time.sleep(SLEEP_SECONDS)

print("All done.")
