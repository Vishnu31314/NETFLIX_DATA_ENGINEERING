import pandas as pd
import pyodbc

# Path to your global CSV file
CSV_PATH = "data/all-weeks-global.csv"

# Azure SQL connection string
SQL_CONN = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=netflix-sql-vishnu.database.windows.net;"
    "DATABASE=netflixdb;"
    "UID=sqladmin;"
    "PWD=Vishnu@123"
)

def load_data():
    # Load CSV
    df = pd.read_csv(CSV_PATH)

    # Parse date column
    df['week'] = pd.to_datetime(df['week'])

    # Connect to SQL Server
    conn = pyodbc.connect(SQL_CONN)
    cursor = conn.cursor()

    for _, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT INTO weekly_global_top10
                (week, category, weekly_rank, show_title, season_title, weekly_hours_viewed, cumulative_weeks_in_top_10)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
                row['week'],
                row['category'],
                int(row['weekly_rank']),
                row['show_title'],
                row['season_title'] if pd.notna(row['season_title']) else None,
                int(row['weekly_hours_viewed']),
                int(row['cumulative_weeks_in_top_10'])
            )
        except Exception as e:
            print(f"❌ Error at row {_}: {e}")

    conn.commit()
    conn.close()
    print("✅ Data loaded successfully.")

if __name__ == "__main__":
    load_data()
