import pytest 
import api
import petl as etl
from unittest.mock import patch 
from datetime import datetime   

def test_read_csv(monkeypatch):

    """Test the api's ability to open a csv and create a petl table abstraction"""

    monkeypatch.setattr("sys.argv", ["sys argument 0", "sys argument 1", "calendar_details.csv"])
    test_calendar_details = api.read_csv()
    assert test_calendar_details
    assert etl.header(test_calendar_details) == ("\ufeffSubject","Start_Date","Start_Time","End_Date","End_Time","All day event","Reminder Date","Reminder Time","Meeting Organizer","Required Attendees","Categories","Description","Location","Month","Length_of_Time")

@pytest.mark.skip()
def test_write_csv(calendar_details):

    #keep in mind you're trying to mock the write method.  Page 141 of python testing book.
    with patch.object(calendar_details, 'calendar_details') as mock_calendar_details:
        csv = api.write_csv(mock_calendar_details)
    assert csv

def test_modify_table_columns(og_csv):

    """Test the api's ability to modify the table columns to rename the column headers for Start Date, Start Time, End Date and End Time.  Also tests that the element in the first row of the Start_Date column is stored as datetime object."""

    modified_table_columns = api.modify_table_columns(og_csv)
    assert etl.header(modified_table_columns) == ("\ufeffSubject","Start_Date","Start_Time","End_Date","End_Time","All day event","Reminder Date","Reminder Time","Meeting Organizer","Required Attendees","Optional Attendees","Meeting Resources","Billing Information","Categories","Description","Location")

    check_start_date = etl.data(modified_table_columns)
    start_date = list(check_start_date)
    assert type(start_date[1][1]) is type(datetime.today())

def test_add_remove_columns(og_csv):

    """Test the api's ability to remove unneeded columns and add a Month and Length_of_Time column.  It also tests that the first element in the Length_of_Time column is stored as a float."""

    modified = api.modify_table_columns(og_csv)
    added_removed_columns = api.add_remove_columns(modified)
    assert etl.header(added_removed_columns) == ("\ufeffSubject","Start_Date","Start_Time","End_Date","End_Time","All day event","Reminder Date","Reminder Time","Meeting Organizer","Required Attendees","Categories","Description","Location","Month","Length_of_Time")

    check_time = etl.data(added_removed_columns)
    length_of_time = list(check_time)
    assert type(length_of_time[1][14]) is type(0.0)

def test_count_rows(calendar_details):

    """Tests the api's ability to count the rows in the table"""

    rows = api.count_rows(calendar_details)
    assert rows == f'file rows: {489}'

def test_quickview(calendar_details):

    """Tests that the api doesn't throw an error when quickview is called"""

    with patch('builtins.input', return_value=5):
        quickview_test = api.quickview(calendar_details)
    assert quickview_test

def test_time_stats(calendar_details, capsys):

    """Tests that the api returns the stats output when the time_stats function is called"""

    api.time_stats(calendar_details)
    output = capsys.readouterr().out.rstrip()
    assert output == "stats(count=489, errors=0, sum=56830.0, min=5.0, max=540.0, mean=116.21676891615543, pvariance=21478.42744886478, pstdev=146.55520273557258)"





