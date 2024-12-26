import pytest
import api
import petl as etl  

#these two tests require a different fixture with an unchanged file to work on 
def test_modify_table_columns():
    #assert column headers were renamed
    #assert Start_Date and Start_Time in a given row is formatted to datetime format
    pass

def test_add_remove_columns():
    #assert the total columns is equal to XX
    pass

def test_count_rows(calendar_details):
    rows = api.count_rows(calendar_details)
    assert rows == f'file rows: {489}'

def test_quickview(calendar_details):
    quickview = etl.cut(calendar_details, 0, "Start_Date", "Length_of_Time")
    headers = etl.header(quickview)
    assert len(headers) == 3
    assert headers == ("\ufeffSubject", "Start_Date", "Length_of_Time")





