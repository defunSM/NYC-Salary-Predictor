
import pandas as pd
import requests
from typing import List


# TODO: Split out the functions so that they are responsible for only one thing
# CHANGED: Moved the parameters to exist in the get_nyc_payroll_data since that makes more sense

def get_nyc_payroll_data(parameters):
    """Requesting the data from the API endpoint returning a dataframe
    
    Example of parameters:
    
    parameters = {
        'fiscal_year': fiscal_year,
        '$$app_token': API_TOKEN_KEY,
        '$limit': limit,
    } 
    
    """
    
    print(f'Getting NYC Payroll data ...')
    
    response = requests.get('https://data.cityofnewyork.us/resource/k397-673e.csv', params=parameters)
    
    return response


    
def convert_dataframe_to_csv(df: pd.DataFrame, filename: str):
    
    df.to_csv(filename, index=False)
    print(f"{filename} successfully created!")
    
# Use spark here to speed up the process    
def read_from_csv_file(filename):
    # Reads a json file and passes it
    df = pd.read_csv(filename)
    return df