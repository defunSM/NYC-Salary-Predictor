import os

from setup_nyc_payroll import download_data

FISCAL_YEAR = 2020
LIMIT = 1000000
FILENAME = 'nyc_payroll.json'

def main():

    # Checks if the FILENAME has already been downloaded
    if not os.path.isfile(FILENAME):
        download_data(FISCAL_YEAR, LIMIT, FILENAME)
    else:
        print(f"Skipping download {FILENAME} exists")

    # Implement reading from FILENAME 

if __name__ == '__main__':
    main()