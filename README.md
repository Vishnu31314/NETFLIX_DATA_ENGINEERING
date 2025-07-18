
# Netflix Data Engineering Project 📊

This project showcases an end-to-end **ETL pipeline** built with Python and Azure SQL Database. It processes Netflix Top 10 viewership data, both globally and by country, and loads it into a cloud-hosted relational database for further analysis.

---

## 💼 Technologies Used
- Python (`pandas`, `pyodbc`)
- Azure SQL Database
- Visual Studio Code
- CSV Data Ingestion

---

## 📁 Data Sources
- `most-popular.csv` – Netflix's all-time most popular titles.
- `all-weeks-global.csv` – Weekly Top 10 titles globally.
- `all-weeks-countries.csv` – Weekly Top 10 titles by country.

---

## 🛠️ ETL Scripts
Located in the `/scripts` folder:
- `etl_popular_to_sql.py` – Loads data into `most_popular_titles`.
- `etl_global_to_sql.py` – Loads data into `weekly_global_top10`.
- `etl_country_to_sql.py` – Loads data into `weekly_country_views`.

---

## 🗃️ SQL Table Scripts
Located in the `/sql` folder:
- `most_popular_titles.sql`
- `weekly_global_top10.sql`
- `weekly_country_top10.sql`

---

## ⚙️ Setup Instructions

1. Create the required tables by running the `.sql` scripts in your Azure SQL DB.
2. Update your connection string and credentials in each Python ETL script.
3. Install dependencies:
   ```bash
   pip install pandas pyodbc
   ```
4. Run an ETL script:
   ```bash
   python scripts/etl_global_to_sql.py
   ```

---

## 📌 Project Purpose

> This project demonstrates practical skills in data engineering, ETL design, cloud SQL management, and Python-based automation — suitable for portfolio and resume.

---

## 🔒 Note
This project uses sample public CSVs and does not require API keys or credentials.
