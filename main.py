import os


from setup_nyc_payroll import download_data, read_from_csv_file

FISCAL_YEAR = 2020
LIMIT = 1000000
FILENAME = 'nyc_payroll.csv'

def main():

    # Checks if the FILENAME has already been downloaded
    if not os.path.isfile(FILENAME):
        payroll_data = download_data(FISCAL_YEAR, LIMIT, FILENAME)
    else:
        print(f"Skipping download {FILENAME} exists")
        payroll_data = read_from_csv_file(FILENAME)

    
    

if __name__ == '__main__':
    main()