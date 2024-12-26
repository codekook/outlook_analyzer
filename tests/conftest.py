import pytest
import os
import petl as etl 
from dotenv import load_dotenv

@pytest.fixture()
def calendar_details():
    
    '''Provide a petl table abstraction in order to test the api functions'''

    load_dotenv()
    route = os.getenv('TEST_ROUTE')

    calendar_details = etl.io.csv.fromcsv(route)
    return calendar_details