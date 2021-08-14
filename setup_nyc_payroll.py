import requests
import json
import pandas as pd

from typing import List
from secrets import API_TOKEN_KEY

# TODO: Remove this at some point
# def write_to_csv_file(data, filename) -> None:
#     # writes the data to a json file to FILENAME
#     print(f"Creating {filename} ...")
#     with open(filename, 'w') as file_object:
#         json.dump(data, file_object)

def get_nyc_payroll_data(parameters) -> requests.Response:
    # requesting the data from the API endpoint
    print(f'Requesting NYC Payroll data ...')
    response = requests.get('https://data.cityofnewyork.us/resource/k397-673e.csv',      params=parameters)

    return response

# TODO: Could probably merge download_data and get_nyc_payroll_data together

def download_data(fiscal_year: int, limit: int, filename: str) -> None:
    # Uses write_to_json_file and get_nyc_payroll_data to create a json file with the data
    print(API_TOKEN_KEY)
    parameters = {
        'fiscal_year': fiscal_year,
        '$$app_token': API_TOKEN_KEY,
        '$limit': limit,
        }

    response = get_nyc_payroll_data(parameters)
    print(response)
    df = pd.DataFrame(response)
    #df.to_csv(filename, index=False)
    
    print(f"{filename} successfully created!")

# TODO Fix read from csv_file so it returns the dataframe of pandas
def read_from_csv_file(filename):
    # Reads a json file and passes it
    df = pd.read_csv(filename)
    return df