import requests
import mysql.connector
from datetime import datetime
import urllib3

# --- 0. Disable SSL warnings (still good practice) ---
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- 1. Connect to MySQL ---
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="busayo123",  # 🔁 Replace with your actual password
    database="job_market_db"
)
cursor = conn.cursor()

# --- 2. Fetch job data from Remotive API ---
url = "https://remotive.com/api/remote-jobs"  # ✅ CORRECTED URL
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)
print("Status code:", response.status_code)
print("Response preview:", response.text[:200])  # Confirm it's JSON

data = response.json()
jobs = data.get("jobs", [])
job_count = 0

for job in jobs:
    title = job.get("title", "N/A")
    company = job.get("company_name", "N/A")
    location = job.get("candidate_required_location", "Remote")
    tags = ", ".join(job.get("tags", []))
    source = "Remotive"
    date_posted = datetime.strptime(job.get("publication_date", "")[:10], "%Y-%m-%d").date()

    print(f"Inserting: {title} | {company} | {location}")

    cursor.execute("""
        INSERT INTO jobs (job_title, company, location, tags, source, date_posted)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (title, company, location, tags, source, date_posted))

    job_count += 1

# --- 3. Finalize ---
conn.commit()
cursor.close()
conn.close()

print(f"✅ Remotive jobs inserted into MySQL: {job_count}")

