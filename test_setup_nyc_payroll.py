import pytest
from setup_nyc_payroll import read_from_file


def test_read_from_file():
    filename = 'nyc_payroll.json'
    print(read_from_file(filename))