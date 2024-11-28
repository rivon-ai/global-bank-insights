import os
import sqlite3
import pandas as pd
from datetime import datetime

def save_data(data, csv_path, db_path, table_name="Largest_banks", log_file="code_log.txt"):
    """
    Save the processed DataFrame to a CSV file and an SQLite database.
    
    Args:
        data (pd.DataFrame): Processed DataFrame to be saved.
        csv_path (str): Path to save the CSV file.
        db_path (str): Path to the SQLite database file.
        table_name (str): Table name for the SQLite database.
        log_file (str): Path to the log file.
    """
    try:
        # Ensure the output directory exists for the CSV file
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)

        # Step 1: Save the DataFrame to a CSV file
        data.to_csv(csv_path, index=False)
        log_message(f"CSV file saved successfully at {csv_path}", log_file)

        # Step 2: Save the DataFrame to an SQLite database
        conn = sqlite3.connect(db_path)
        data.to_sql(table_name, conn, if_exists="replace", index=False)
        conn.close()
        log_message(f"Data saved successfully to SQLite database ({db_path}) in table '{table_name}'", log_file)

    except Exception as e:
        log_message(f"Error saving data: {e}", log_file)
        raise

def log_message(message, log_file):
    """
    Log a message to the specified log file with a timestamp.
    
    Args:
        message (str): Message to be logged.
        log_file (str): Path to the log file.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as file:
        file.write(f"[{timestamp}] {message}\n")
    print(message)  # Optional: Print the message for real-time feedback
