import os

from setup_nyc_payroll import download_data, read_from_file

FISCAL_YEAR = 2020
LIMIT = 1000000
FILENAME = 'nyc_payroll.json'

def main():

    # Checks if the FILENAME has already been downloaded
    if not os.path.isfile(FILENAME):
        download_data(FISCAL_YEAR, LIMIT, FILENAME)
    else:
        print(f"Skipping download {FILENAME} exists")

    # Taking the json data from FILENAME. 

    payroll_data = read_from_file(FILENAME)
    #print(payroll_data)

if __name__ == '__main__':
    main()