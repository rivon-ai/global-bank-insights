import os
import sqlite3
import pandas as pd
from scripts.logging_utils import log_message 

def save_data(data, csv_path, db_path, table_name="Largest_banks", log_file="logs/code_log.txt"):
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
        os.makedirs(os.path.dirname(csv_path), exist_ok=True)
        
        data.to_csv(csv_path, index=False)
        log_message(f"CSV file saved successfully at {csv_path}", log_file)
        conn = sqlite3.connect(db_path)
        data.to_sql('Largest_banks', conn, if_exists='replace', index=False)
        conn.commit()
        log_message(f"Data saved successfully to SQLite database ({db_path}) in table '{table_name}'", log_file)

    except Exception as e:
        log_message(f"Error saving data: {e}", log_file)
        raise