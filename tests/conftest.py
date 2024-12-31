import pytest
import os
import petl as etl 
from dotenv import load_dotenv

@pytest.fixture()
def calendar_details():
    
    '''Provide a modified petl table abstraction in order to test the api functions'''

    load_dotenv()
    calendar_csv_file = os.getenv('TEST_CSV')
    return etl.io.csv.fromcsv(calendar_csv_file)

@pytest.fixture()
def og_csv():

    '''Provide an unmodified version of the csv file in order to test modification functions'''

    load_dotenv()
    og_csv_file = os.getenv('TEST_OG_CSV')
    return etl.io.csv.fromcsv(og_csv_file)

