import requests
from bs4 import BeautifulSoup
import mysql.connector
from datetime import datetime

# --- 1. Connect to MySQL ---
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="busayo123",  # 🔁 Replace with your actual MySQL root password
    database="job_market_db"
)
cursor = conn.cursor()

# --- 2. Scrape We Work Remotely jobs ---
url = "https://weworkremotely.com/categories/remote-programming-jobs"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Select the job sections
jobs_section = soup.select("section.jobs article")

job_count = 0

for article in jobs_section:
    list_items = article.select("ul li")

    for job in list_items:
        anchor = job.find("a", href=True)
        if not anchor:
            continue

        title_span = job.find("span", class_="title")
        company_span = job.find("span", class_="company")
        region_span = job.find("span", class_="region company")

        title = title_span.text.strip() if title_span else "N/A"
        company = company_span.text.strip() if company_span else "N/A"
        location = region_span.text.strip() if region_span else "Remote"
        tags = "Programming"
        date_posted = datetime.today().date()
        source = "WeWorkRemotely"

        # ✅ Print each job before inserting
        print(f"Inserting: {title} | {company} | {location}")

        # Insert into MySQL
        cursor.execute("""
            INSERT INTO jobs (job_title, company, location, tags, source, date_posted)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (title, company, location, tags, source, date_posted))

        job_count += 1

# Finalize
conn.commit()
cursor.close()
conn.close()

print(f"✅ WeWorkRemotely jobs inserted into MySQL: {job_count}")

