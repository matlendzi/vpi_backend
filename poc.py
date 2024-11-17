import pandas as pd
import sqlite3
import os

# Path to the SQLite database file
DATABASE_PATH = "poc_data.db"

# Path to the folder containing CSV files to be imported
DATA_FOLDER = "./data"

# Establish a connection to the SQLite database
conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

# Create the necessary tables in the database if they don't already exist

# Table for storing age group data
cursor.execute("""
    CREATE TABLE IF NOT EXISTS age_data (
        id INTEGER,           -- Unique identifier for each record
        zone_id TEXT,         -- Zone identifier
        hour TEXT,            -- Hour of the data collection
        weekday TEXT,         -- Weekday of the data collection
        quarter TEXT,         -- Quarter of the year
        visitors REAL,        -- Number of visitors
        date TEXT,            -- Date of the record
        age_group TEXT        -- Age group of the visitors
    )
""")

# Table for storing dwell time data
cursor.execute("""
    CREATE TABLE IF NOT EXISTS dwelltime_data (
        id INTEGER,           -- Unique identifier for each record
        hour TEXT,            -- Hour of the data collection
        weekday TEXT,         -- Weekday of the data collection
        quarter TEXT,         -- Quarter of the year
        visitors REAL,        -- Number of visitors
        date TEXT,            -- Date of the record
        zone_id TEXT,         -- Zone identifier
        DwellTime TEXT        -- Dwell time category of the visitors
    )
""")

# Table for storing gender data
cursor.execute("""
    CREATE TABLE IF NOT EXISTS gender_data (
        id INTEGER,           -- Unique identifier for each record
        zone_id TEXT,         -- Zone identifier
        hour TEXT,            -- Hour of the data collection
        weekday TEXT,         -- Weekday of the data collection
        quarter TEXT,         -- Quarter of the year
        visitors REAL,        -- Number of visitors
        date TEXT,            -- Date of the record
        gender TEXT           -- Gender of the visitors
    )
""")

# Table for storing visitor type data
cursor.execute("""
    CREATE TABLE IF NOT EXISTS visitortype_data (
        id INTEGER,           -- Unique identifier for each record
        hour TEXT,            -- Hour of the data collection
        weekday TEXT,         -- Weekday of the data collection
        quarter TEXT,         -- Quarter of the year
        visitors REAL,        -- Number of visitors
        date TEXT,            -- Date of the record
        zone_id TEXT,         -- Zone identifier
        VisitorType TEXT      -- Visitor type (e.g., tourist, local, etc.)
    )
""")

# Table for storing zip origin data
cursor.execute("""
    CREATE TABLE IF NOT EXISTS ziporigin_data (
        id INTEGER,           -- Unique identifier for each record
        zone_id TEXT,         -- Zone identifier
        hour TEXT,            -- Hour of the data collection
        weekday TEXT,         -- Weekday of the data collection
        quarter TEXT,         -- Quarter of the year
        visitors REAL,        -- Number of visitors
        date TEXT,            -- Date of the record
        zip_code TEXT,        -- ZIP code of the origin
        use TEXT              -- Type of use (e.g., residential, business, etc.)
    )
""")

# Process each CSV file in the data folder
for filename in os.listdir(DATA_FOLDER):
    file_path = os.path.join(DATA_FOLDER, filename)

    # Skip empty files
    if os.stat(file_path).st_size == 0:
        print(f"Skipped {filename} because it is empty.")
        continue

    # Import data into the corresponding table based on the file prefix
    if filename.startswith("Hamburg_age"):
        df = pd.read_csv(file_path)
        print(f"Processing {filename}:")
        print(df.head())  # Display the first few rows of the data
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

# Create indexes to optimize queries
cursor.execute("CREATE INDEX IF NOT EXISTS idx_age_zone_id_date ON age_data (zone_id, date);")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_dwelltime_zone_id_date ON dwelltime_data (zone_id, date);")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_visitortype_zone_id_date ON visitortype_data (zone_id, date);")

# Add additional indexes for specific filterable columns
cursor.execute("CREATE INDEX IF NOT EXISTS idx_age_group ON age_data (age_group);")
cursor.execute("CREATE INDEX IF NOT EXISTS idx_dwelltime ON dwelltime_data (DwellTime);")

# Commit the changes to the database and close the connection
conn.commit()
conn.close()
print("All data imported and indexed.")
