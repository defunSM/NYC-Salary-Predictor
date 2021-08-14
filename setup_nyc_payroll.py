import requests
import json
from typing import List

from secrets import API_TOKEN_KEY

def write_to_json_file(data, filename) -> None:
    # writes the data to a json file to FILENAME
    print(f"Creating {filename} ...")
    with open(filename, 'w') as file_object:
        json.dump(data, file_object)


def get_nyc_payroll_data(parameters) -> requests.Response:
    # requesting the data from the API endpoint
    print(f'Requesting NYC Payroll data ...')
    response = requests.get('https://data.cityofnewyork.us/resource/k397-673e.json', params=parameters)

    return response


def download_data(fiscal_year: int, limit: int, filename: str) -> None:
    # Uses write_to_json_file and get_nyc_payroll_data to create a json file with the data
    print(API_TOKEN_KEY)
    parameters = {
        'fiscal_year': fiscal_year,
        '$$app_token': API_TOKEN_KEY,
        '$limit': limit,
        }

    response = get_nyc_payroll_data(parameters)
    data = response.json()

    write_to_json_file(data)
    
    print(f"{filename} successfully created!")

def read_from_file(filename) -> List:
    # Reads a json file and passes it
    with open(filename, 'r') as file_object:
        json_data = json.load(file_object)

    return json_data