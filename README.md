# 📊 Netflix Data Engineering Project

This project showcases an end-to-end **ETL pipeline** built with **Python** and **Azure SQL Database**. It processes Netflix Top 10 viewership data, both globally and by country, and loads it into a cloud-hosted SQL database for analysis.

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

## 🛠️ ETL Scripts (in `/scripts`)
- `etl_popular_to_sql.py` → Loads into `most_popular_titles`
- `etl_global_to_sql.py` → Loads into `weekly_global_top10`
- `etl_country_to_sql.py` → Loads into `weekly_country_top10`

---

## 🗃️ SQL Table Scripts (in `/sql`)
- `most_popular_titles.sql`
- `weekly_global_top10.sql`
- `weekly_country_top10.sql`

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/your-username/netflix-data-engineering.git
cd netflix-data-engineering
```

### 2. Create Azure SQL tables
Run the `.sql` files in your Azure Query Editor or SQL Server Management Studio (SSMS).

### 3. Set up your Python environment
Install dependencies from the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 4. Configure database credentials
Update the `SQL_CONN` string in each Python script with your Azure SQL details:
```python
SQL_CONN = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=your-server.database.windows.net;"
    "DATABASE=netflixdb;"
    "UID=your-username;"
    "PWD=your-password"
)
```

### 5. Run the ETL pipeline
```bash
python scripts/etl_global_to_sql.py
python scripts/etl_country_to_sql.py
python scripts/etl_popular_to_sql.py
```

---

## 📌 Project Purpose

> This project demonstrates skills in **data engineering**, **ETL pipelines**, **cloud SQL integration**, and **Python automation**. Ideal for showcasing in portfolios and resumes.

---

## 📦 Requirements

A `requirements.txt` file should be included:

```txt
pandas
pyodbc
```

Generate it with:
```bash
pip freeze > requirements.txt
```

---

## 🔒 Note
This project uses **public CSV datasets only**. No API keys or credentials are required.

---

## 🔗 Author
**Vishnu Jangid**  

