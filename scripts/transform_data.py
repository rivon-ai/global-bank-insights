import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
EXCHANGE_RATES = {
    'GBP': float(os.getenv("EXCHANGE_RATE_GBP", 0.0)),
    'EUR': float(os.getenv("EXCHANGE_RATE_EUR", 0.0)),
    'INR': float(os.getenv("EXCHANGE_RATE_INR", 0.0))
}

def transform_data(data):
    """Transform MC_USD_Billion into GBP, EUR, and INR using exchange rates.

    Args:
        data (pd.DataFrame): Input DataFrame with `MC_USD_Billion` column.

    Returns:
        pd.DataFrame: Transformed DataFrame with additional columns for GBP, EUR, and INR.
    """
    if not all(EXCHANGE_RATES.values()):
        raise ValueError("One or more exchange rates are missing or invalid in the .env file.")
    
    data['MC_USD_Billion'] = (
        data['MC_USD_Billion'].replace('[\$,]', '', regex=True).astype(float)
        )

    data['MC_GBP_Billion'] = (data['MC_USD_Billion'] * EXCHANGE_RATES['GBP']).round(2)
    data['MC_EUR_Billion'] = (data['MC_USD_Billion'] * EXCHANGE_RATES['EUR']).round(2)
    data['MC_INR_Billion'] = (data['MC_USD_Billion'] * EXCHANGE_RATES['INR']).round(2)

    return data
