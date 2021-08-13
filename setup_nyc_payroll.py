import requests
import json

from secrets import API_TOKEN_KEY

# writes the data to a json file to FILENAME
def write_to_json_file(data, filename):
    print(f"Creating {filename} ...")
    with open(filename, 'w') as file_object:
        json.dump(data, file_object)

# requesting the data from the API endpoint
def get_nyc_payroll_data(parameters):
    print(f'Requesting NYC Payroll data ...')
    response = requests.get('https://data.cityofnewyork.us/resource/k397-673e.json', params=parameters)

    return response

# Uses write_to_json_file and get_nyc_payroll_data to create a json file with the data
def download_data(fiscal_year: int, limit: int, filename: str):
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


