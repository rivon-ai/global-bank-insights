import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv("API_URL")
if not URL:
    print("Error: API_URL not found in the .env file. Please add it.")
    exit()

def fetch_html(url):
    """Fetch HTML content from the provided URL."""
    try:
        response = requests.get(url)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        exit()

def parse_table(html):
    """Parse the HTML to extract bank data from the table."""
    soup = BeautifulSoup(html, "html.parser")
    try:
        table = soup.find("table", {"class": "wikitable sortable mw-collapsible"})
        rows = table.find("tbody").find_all("tr")
    except AttributeError:
        print("Error: Unable to locate the table in the HTML.")
        exit()
    
    bank_names = []
    market_caps = []
    for row in rows[1:]:
        columns = [col.text.strip() for col in row.find_all("td")]
        if len(columns) >= 3:
            bank_names.append(columns[1])  
            market_caps.append(columns[2]) 

    return pd.DataFrame({"Name": bank_names, "MC_USD_Billion": market_caps})

def extract_data():
    """Extracts data and returns it as a DataFrame."""
    html = fetch_html(URL)
    return parse_table(html)

