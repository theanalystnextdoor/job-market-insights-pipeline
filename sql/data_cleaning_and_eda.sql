-- =====================================
-- 🧹 DATA CLEANING + EXPLORATORY ANALYSIS
-- Project: Job Market Insights Pipeline
-- Author: Kolawole Olaitan
-- Date: August 2025
-- =====================================

-- ✅ Use the correct database
USE job_market_db;

-- -------------------------------------
-- 🔍 1. CHECK FOR MISSING VALUES
-- -------------------------------------
SELECT
  COUNT(*) AS total_rows,
  SUM(job_title IS NULL OR job_title = '') AS null_job_titles,
  SUM(company IS NULL OR company = '') AS null_companies,
  SUM(location IS NULL OR location = '') AS null_locations,
  SUM(tags IS NULL OR tags = '') AS null_tags
FROM jobs;

-- -------------------------------------
-- 🗑️ 2. REMOVE ROWS WITH MISSING JOB TITLE OR COMPANY
-- -------------------------------------
DELETE FROM jobs
WHERE job_title IS NULL OR job_title = ''
   OR company IS NULL OR company = '';

-- -------------------------------------
-- 🔄 3. REMOVE DUPLICATES (same job_title, company, date)
-- Keeping the row with the lowest ID
-- -------------------------------------
DELETE j1 FROM jobs j1
JOIN jobs j2 ON
  j1.job_title = j2.job_title AND
  j1.company = j2.company AND
  j1.date_posted = j2.date_posted AND
  j1.id > j2.id;

-- -------------------------------------
-- 📊 4. MOST FREQUENT JOB TITLES
-- -------------------------------------
SELECT job_title, COUNT(*) AS postings
FROM jobs
GROUP BY job_title
ORDER BY postings DESC
LIMIT 10;

-- -------------------------------------
-- 🏢 5. MOST FREQUENT COMPANIES POSTING JOBS
-- -------------------------------------
SELECT company, COUNT(*) AS postings
FROM jobs
GROUP BY company
ORDER BY postings DESC
LIMIT 10;

-- -------------------------------------
-- 🗓️ 6. JOB COUNTS PER DAY
-- -------------------------------------
SELECT date_posted, COUNT(*) AS job_count
FROM jobs
GROUP BY date_posted
ORDER BY date_posted DESC;

-- -------------------------------------
-- 🌍 7. LONGEST LOCATIONS (For display issues)
-- -------------------------------------
SELECT location, LENGTH(location) AS length
FROM jobs
ORDER BY length DESC
LIMIT 5;

-- -------------------------------------
-- 🧾 8. CHECK JOB SOURCE DISTRIBUTION
-- -------------------------------------
SELECT source, COUNT(*) AS total
FROM jobs
GROUP BY source;

-- ✅ End of script
