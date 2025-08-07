# 💼 Job Market Insights Pipeline

This project scrapes job listings from multiple websites, stores them in a MySQL database, and is designed to support future job trend insights and visualizations.

---

## 🚀 Tools & Technologies

- **Python** – Web scraping and automation
- **MySQL** – Structured data storage
- **Git & GitHub** – Version control
- **Power BI** – (Optional) Visualization

---

## 📂 Project Structure

job-market-insights-pipeline/
│
├── scraper/ # Web scraping scripts (RemoteOK & Remotive)
├── sql/ # SQL schema setup and cleaning
├── etl/ # ETL logic (optional/placeholder)
├── dashboard/ # Power BI reports (optional)
├── requirements.txt # Python package requirements
└── README.md # Project documentation


---

## 🌍 Data Sources

- [RemoteOK API](https://remoteok.com/api)
- [Remotive API](https://remotive.io/api/remote-jobs)

❌ Note: WeWorkRemotely could not be scraped due to Cloudflare protections.

---

## ⚠️ Limitations

- The project currently scrapes only one day's worth of job data.
- Further automation (e.g., scheduled scraping) will improve data quality and insight depth.

---

## 🧠 Project Goals

- Practice data engineering principles (web scraping → storing → transforming)
- Explore SQL for data cleaning and analysis
- Showcase technical proficiency in building end-to-end data pipelines

---

---

## 🧠 Behind the Logic

### 1. 🔍 Web Scraping Logic

Each scraping script (`remoteok_scraper.py` and `remotive_scraper.py`) follows a clean and modular approach:

- **HTTP Requests**: Uses `requests` with custom headers to simulate a browser and avoid being blocked.
- **JSON Parsing**: Parses the API response directly, which is cleaner and more stable than scraping raw HTML.
- **Error Handling**: Basic try-except blocks (planned for improvement).
- **Data Extraction**: Extracts relevant fields like job title, company, location, tags, and posted date.

### 2. 🛢️ MySQL Storage

- **Schema Design**: A single `jobs` table was created to store the scraped data consistently.
- **Constraints**: Column size limits were optimized after discovering overly long values (e.g., `location` column).
- **Connection**: Python’s `mysql.connector` library is used to insert records into the MySQL database.
- **Deduplication**: Basic checks (e.g., on job title + company) can be added in the future to avoid duplicates.

### 3. 🔁 ETL Flow

Though simple, this project follows a basic ETL (Extract, Transform, Load) model:

- **Extract**: Pull data from RemoteOK and Remotive APIs.
- **Transform**: Clean fields (e.g., combine tags, format dates).
- **Load**: Insert into a structured MySQL database.

Future improvements could include:
- Scheduled jobs (via cron or Airflow)
- Staging tables for raw vs. cleaned data
- Detailed logging and retries

## 🛠️ How to Run

1. **Clone the repository**
```bash
git clone https://github.com/theanalystnextdoor/job-market-insights-pipeline.git
Install dependencies

bash

pip install -r requirements.txt
Run scraping scripts

bash

python scraper/remoteok_scraper.py
python scraper/remotive_scraper.py

View & analyze data

Load the database in MySQL Workbench

Connect to Power BI for future dashboarding (optional)

📈 Next Steps
Schedule daily/weekly scraping to collect historical job market data

Perform advanced text cleaning or NLP on job titles/descriptions

Deploy dashboards publicly (Power BI Service or Streamlit)

👨‍💻 Author
Kolawole Olaitan
Data Analyst | Portfolio Project
🔗 LinkedIn
