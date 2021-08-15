import requests
import json
import asyncio
import aiohttp
import time

from typing import List
from secrets import API_TOKEN_KEY

def timer(func):
    # Used as a decorator to help time get_nyc_payroll_data
    def wrapper(*args):
        start = time.time()
        func(args, args[-1])
        print(time.time() - start)
    return wrapper

def write_to_json_file(data, filename) -> None:
    # writes the data to a json file to FILENAME
    print(f"Creating {filename} ...")
    with open(filename, 'w') as file_object:
        json.dump(data, file_object)


# TODO: Use aiohttp and asyncio to speed up this 

async def get_nyc_payroll_data(parameters, filename):
    # requesting the data from the API endpoint
    print(f'Requesting NYC Payroll data ...')
    
    async with aiohttp.ClientSession() as session:
        async with session.get('https://data.cityofnewyork.us/resource/k397-673e.json', params=parameters) as response:
            data = await response.json()
            write_to_json_file(data, filename)
            
            
def download_data(fiscal_year: int, limit: int, filename: str) -> None:
    # Uses write_to_json_file and get_nyc_payroll_data to create a json file with the data
    print(API_TOKEN_KEY)
    parameters = {
        'fiscal_year': fiscal_year,
        '$$app_token': API_TOKEN_KEY,
        '$limit': limit,
        }
    
    start = time.time()
    asyncio.run(get_nyc_payroll_data(parameters, filename))
    print(time.time() - start)
    
    print(f"{filename} successfully created!")

def read_from_file(filename):
    # Reads a json file and passes it
    with open(filename, 'r') as file_object:
        json_data = json.load(file_object)

    return json_data