# Script to Download Daily Financial JSON Responses Over Multiple Days

This script automates fetching daily financial data from the **Lightspeed K-Series API**.  
It iterates through a specified date range, makes authenticated API requests for each day, and saves each response as an individual JSON file.

---

## 📋 Prerequisites

Before you begin, make sure you have:

1. A **Lightspeed K-Series** account and **API client** set up  
2. **API access** to the `dailyFinancials` endpoint  
3. A valid **access token (Bearer token)**

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/lightspeed-daily-financials.git
````

### 2. Move into the folder

```bash
cd lightspeed-daily-financials
```

### 3. Copy the example environment file

```bash
cp .env.example .env
```

### 4. Fill out the `.env` variables

Open `.env` in your editor and set:

```bash
BASE_URL=https://api.trial.lsk.lightspeed.app/f/finance
BUSINESS_LOCATION_ID=your_business_location_id
AUTH_TOKEN=your_access_token
INCLUDE_PARAMS=payments,consumer
START_DATE=2025-10-09
END_DATE=2025-10-21
SLEEP_SECONDS=1
```

### 5. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

### 6. Install dependencies

```bash
pip install -r requirements.txt
```

or manually using

```bash
pip install python-dotenv requests
```

### 7. Run the script

```bash
python app.py
```

---

## 🗂️ Output

Each API response is saved as a JSON file in the `financials/` folder:

```
financials/
 ├── dailyFinancials_2025-10-09.json
 ├── dailyFinancials_2025-10-10.json
 └── ...
```

An `error_log.txt` file is also generated in the same folder if any requests fail.

---

## 🧩 Notes

* The script reads configuration values from `.env` using [`python-dotenv`](https://pypi.org/project/python-dotenv/).
* You can easily adjust date ranges or include parameters without touching the code.
* To merge all daily JSON files later, you can use:

  ```python
  import glob, json
  data = [json.load(open(f)) for f in sorted(glob.glob("financials/*.json"))]
  json.dump(data, open("merged_financials.json", "w"), indent=2)
  ```

---

## 🧰 Requirements

* Python 3.8 or higher
* `requests`
* `python-dotenv`

---

## ⚠️ Security Tip

Never commit your `.env` file or access token to Git.
A sample `.gitignore` is included to help protect sensitive credentials.
