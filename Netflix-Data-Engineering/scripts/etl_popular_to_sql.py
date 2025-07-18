import pandas as pd
import pyodbc

CSV_PATH = "data/most-popular.csv"

SQL_CONN = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=netflix-sql-vishnu.database.windows.net;"
    "DATABASE=netflixdb;"
    "UID=sqladmin;"
    "PWD=Vishnu@123"
)

def load_data():
    df = pd.read_csv(CSV_PATH)

    # Clean numeric columns
    df['rank'] = pd.to_numeric(df['rank'], errors='coerce')
    df['hours_viewed_first_28_days'] = pd.to_numeric(df['hours_viewed_first_28_days'], errors='coerce')

    # Fill NaN in text columns with None (for SQL NULL)
    df['category'] = df['category'].where(pd.notnull(df['category']), None)
    df['show_title'] = df['show_title'].where(pd.notnull(df['show_title']), None)
    df['season_title'] = df['season_title'].where(pd.notnull(df['season_title']), None)

    conn = pyodbc.connect(SQL_CONN)
    cursor = conn.cursor()

    for index, row in df.iterrows():
        try:
            cursor.execute("""
                INSERT INTO most_popular_titles (
                    category,
                    rank,
                    show_title,
                    season_title,
                    hours_viewed_first_28_days
                )
                VALUES (?, ?, ?, ?, ?)
            """,
            row['category'],
            int(row['rank']) if pd.notnull(row['rank']) else None,
            row['show_title'],
            row['season_title'],
            float(row['hours_viewed_first_28_days']) if pd.notnull(row['hours_viewed_first_28_days']) else None)
        except Exception as e:
            print(f"❌ Error at row {index}: {e}")

    conn.commit()
    conn.close()
    print("✅ Most popular titles loaded successfully!")

if __name__ == "__main__":
    load_data()
