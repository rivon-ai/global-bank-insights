from scripts.extract_data import extract_data
from scripts.transform_data import transform_data
from scripts.save_data import save_data
from scripts.query_data import query_regional_data
import os
from dotenv import load_dotenv
load_dotenv()

def main():
    """Main entry point of the application."""
    # Step 1: Extract data
    data = extract_data()

    # Step 2: Transform data
    transformed_data = transform_data(data)
    
    # Step 3: Save the transformed data
    csv_path = os.getenv("csv_path")
    db_path = os.getenv("db_path")
    log_file = os.getenv("log_file")

    save_data(transformed_data, csv_path, db_path, log_file)
    
    # Step 4: Querying data
    query_regional_data()

    # Step 3: Display the transformed DataFrame
    print("Transformed DataFrame:")
    print(transformed_data)

if __name__ == "__main__":
    main()
