import pandas as pd
import sqlite3
import os

DATABASE_PATH = "poc_data.db"
DATA_FOLDER = "./data"

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS age_data (
        id INTEGER,
        zone_id TEXT,
        hour TEXT,
        weekday TEXT,
        quarter TEXT,
        visitors REAL,
        date TEXT,
        age_group TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS dwelltime_data (
        id INTEGER,
        hour TEXT,
        weekday TEXT,
        quarter TEXT,
        visitors REAL,
        date TEXT,
        zone_id TEXT,
        DwellTime TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS gender_data (
        id INTEGER,
        zone_id TEXT,
        hour TEXT,
        weekday TEXT,
        quarter TEXT,
        visitors REAL,
        date TEXT,
        gender TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS visitortype_data (
        id INTEGER,
        hour TEXT,
        weekday TEXT,
        quarter TEXT,
        visitors REAL,
        date TEXT,
        zone_id TEXT,
        VisitorType TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS ziporigin_data (
        id INTEGER,
        zone_id TEXT,
        hour TEXT,
        weekday TEXT,
        quarter TEXT,
        visitors REAL,
        date TEXT,
        zip_code TEXT,
        use TEXT
    )
""")

for filename in os.listdir(DATA_FOLDER):
    file_path = os.path.join(DATA_FOLDER, filename)

    if os.stat(file_path).st_size == 0:
        print(f"Skipped {filename} because it is empty.")
        continue

    if filename.startswith("Hamburg_age"):
        df = pd.read_csv(file_path)
        print(f"Processing {filename}:")
        print(df.head())
        df.to_sql("age_data", conn, if_exists="append", index=False)
    elif filename.startswith("Hamburg_dwelltime"):
        df = pd.read_csv(file_path)
        print(f"Processing {filename}:")
        print(df.head())
        df.to_sql("dwelltime_data", conn, if_exists="append", index=False)
    elif filename.startswith("Hamburg_gender"):
        df = pd.read_csv(file_path)
        print(f"Processing {filename}:")
        print(df.head())
        df.to_sql("gender_data", conn, if_exists="append", index=False)
    elif filename.startswith("Hamburg_visitortype"):
        df = pd.read_csv(file_path)
        print(f"Processing {filename}:")
        print(df.head())
        df.to_sql("visitortype_data", conn, if_exists="append", index=False)
    elif filename.startswith("Hamburg_ziporigin"):
        df = pd.read_csv(file_path)
        print(f"Processing {filename}:")
        print(df.head())
        df.to_sql("ziporigin_data", conn, if_exists="append", index=False)

conn.commit()
conn.close()
print("All data imported and indexed.")

