import pandas as pd
import pyodbc

CSV_PATH = "../data/all-weeks-global.csv"

SQL_CONN = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=netflix-sql-vishnu.database.windows.net;"
    "DATABASE=netflixdb;"
    "UID=sqladmin;"
    "PWD=Vishnu@123"
)

def load_data():
    print("📥 Starting data load...")

    # Step 1: Load CSV
    try:
        df = pd.read_csv(CSV_PATH)
        print("✅ CSV file loaded")
    except Exception as e:
        print(f"❌ Failed to load CSV: {e}")
        return

    # Step 2: Format date column
    try:
        df['week'] = pd.to_datetime(df['week'])
        print("📆 Date column formatted")
    except Exception as e:
        print(f"❌ Date formatting error: {e}")
        return

    # Step 3: Connect to SQL Server
    try:
        conn = pyodbc.connect(SQL_CONN)
        cursor = conn.cursor()
        print("🔌 Connected to SQL Server")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return

    # Step 4: Insert records
    success_count = 0
    error_count = 0
    for index, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT INTO weekly_global_top10
                (week, category, weekly_rank, show_title, season_title, weekly_hours_viewed, cumulative_weeks_in_top_10)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, row['week'], row['category'], int(row['weekly_rank']), row['show_title'], row['season_title'],
                 int(row['weekly_hours_viewed']), int(row['cumulative_weeks_in_top_10']))
            success_count += 1
            if index % 100 == 0:
                print(f"✅ Inserted {index} records...")
        except Exception as e:
            print(f"❌ Error at row {index}: {e}")
            error_count += 1

    conn.commit()
    conn.close()

    print(f"🎉 Done: {success_count} records inserted, {error_count} errors")

if __name__ == "__main__":
    load_data()
