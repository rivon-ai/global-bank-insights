# Global Bank Insights

![Visitors](https://api.visitorbadge.io/api/visitors?path=global-bank-insights&label=Visitors&countColor=%230d76a8&style=flat&labelStyle=none)
[![License](https://img.shields.io/badge/License-Apache_2.0-0D76A8?style=flat)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.11](https://img.shields.io/badge/Python-3.11-green.svg)](https://shields.io/)

**Global Bank Insights** is a data engineering project designed to extract and process information on the world's largest banks. This pipeline uses web scraping, data transformations, and database storage to deliver actionable insights, including an AI-powered text-to-SQL feature.

---

## **Features**
- **Web Scraping**: Extract real-world data from a public website.
- **Data Transformation**: Convert market capitalization values into multiple currencies (USD, GBP, EUR, INR).
- **Storage**: Save data in CSV and SQLite formats.
- **Database Querying**: Predefined and AI-powered text-to-SQL queries.
- **Streamlit App**: User-friendly interface for querying data.

---

## **Project Structure**

```plaintext
global-bank-insights/
│
├── config/                 # Configuration files
│   ├── db_config.yaml      # Database configuration
│   └── exchange_rate.csv   # Exchange rate data
│
├── data/                   # Data storage
│   ├── raw/                # Raw scraped data
│   └── processed/          # Transformed and final data
│
├── scripts/                # Core scripts
│   ├── extract_data.py     # Web scraping logic
│   ├── transform_data.py   # Data transformation logic
│   ├── save_data.py        # Save data to CSV and SQLite
│   ├── query_data.py       # Query execution logic
│   ├── logging_utils.py    # Logging functionalities
│   ├── text_to_sql.py      # AI-powered text-to-SQL feature
│   └── app.py              # Streamlit application
│
├── logs/                   # Log files for tracking progress
│   └── code_log.txt
│
├── requirements.txt        # Python dependencies
├── banks_project.py        # Main execution script
├── README.md               # Project documentation
└── .gitignore              # Ignore unnecessary files
```

**Prerequisites**
- Python 3.11 or above
- Required libraries (install via requirements.txt)
