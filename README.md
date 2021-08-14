# nyc_payroll
A revised machine learning project that was made for a hackathon using nyc citywide payroll data. (https://opendata.cityofnewyork.us)

## How to use

Create a secrets.py file and store the API_TOKEN_KEY from https://opendata.cityofnewyork.us/data/

```
python -m venv env
source env/bin/activate

pip install -r requirements.txt
python main.py
```

## What is it?

A multiple linear regression model to predict NYC employee salaries.  
