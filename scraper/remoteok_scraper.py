import requests
import mysql.connector
from datetime import datetime

# --- 1. MySQL connection setup ---
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="busayo123",  # <-- Use your correct MySQL password here
    database="job_market_db"
)
cursor = conn.cursor()

# --- 2. Fetch job data from RemoteOK ---
url = "https://remoteok.com/api"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
jobs = response.json()

# --- 3. Insert job records ---
for job in jobs[1:]:  # skip metadata
    title = job.get('position', 'N/A')
    company = job.get('company', 'N/A')
    location = job.get('location') or "Remote"
    tags = ", ".join(job.get('tags', []))
    source = "RemoteOK"
    date_str = job.get('date') or datetime.today().strftime('%Y-%m-%d')
    date_posted = datetime.strptime(date_str[:10], "%Y-%m-%d").date()

    cursor.execute("""
        INSERT INTO jobs (job_title, company, location, tags, source, date_posted)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (title, company, location, tags, source, date_posted))

# --- 4. Finalize ---
conn.commit()
cursor.close()
conn.close()

print("✅ RemoteOK jobs inserted into MySQL!")


