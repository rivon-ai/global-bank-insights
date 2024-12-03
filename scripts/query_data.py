import sqlite3
import pandas as pd
from dotenv import load_dotenv
import os
from scripts.logging_utils import log_message

load_dotenv()
db_path = os.getenv("db_path")
log_file = os.getenv("log_file")
table_name = "Largest_banks"

def check_table_exists(conn):
    """Check if the table exists in the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    return cursor.fetchone()

def query_regional_data():
    try:
        conn = sqlite3.connect(db_path)
        log_message("Connected to SQLite database.", log_file)

        if not check_table_exists(conn):
            print(f"Error: Table '{table_name}' does not exist in the database.")
            log_message(f"Error: Table '{table_name}' does not exist in the database.", log_file)
            return

        regional_queries = {
            "London Office": f"SELECT Name, MC_GBP_Billion FROM {table_name} WHERE MC_GBP_Billion IS NOT NULL",
            "Berlin Office": f"SELECT Name, MC_EUR_Billion FROM {table_name} WHERE MC_EUR_Billion IS NOT NULL",
            "New Delhi Office": f"SELECT Name, MC_INR_Billion FROM {table_name} WHERE MC_INR_Billion IS NOT NULL",
        }
        for office, query in regional_queries.items():
            print(f"\n--- {office} ---")
            query_output = pd.read_sql(query, conn)
            print(query_output)
        conn.close()
        log_message("SQLite database connection closed.", log_file)

    except sqlite3.Error as e:
        log_message(f"Error: {e}", log_file)
        print(f"Error: {e}")