import pytest
import api
import petl as etl
import os
from unittest.mock import patch 
from dotenv import load_dotenv   
 
def test_modify_table_columns(og_csv):
    modified_table_columns = api.modify_table_columns(og_csv)
    assert etl.header(modified_table_columns) == ("\ufeffSubject","Start_Date","Start_Time","End_Date","End_Time","All day event","Reminder Date","Reminder Time","Meeting Organizer","Required Attendees","Optional Attendees","Meeting Resources","Billing Information","Categories","Description","Location")

def test_add_remove_columns(og_csv):
    modified = api.modify_table_columns(og_csv)
    added_removed_columns = api.add_remove_columns(modified)
    assert etl.header(added_removed_columns) == ("\ufeffSubject","Start_Date","Start_Time","End_Date","End_Time","All day event","Reminder Date","Reminder Time","Meeting Organizer","Required Attendees","Categories","Description","Location", "Month", "Length_of_Time")

def test_count_rows(calendar_details):
    rows = api.count_rows(calendar_details)
    assert rows == f'file rows: {489}'

def test_quickview(calendar_details):
    with patch('builtins.input', return_value=5):
        quickview_test = api.quickview(calendar_details)
    assert quickview_test

def test_time_stats(calendar_details):
    stats = etl.stats(calendar_details, "Length_of_Time")
    assert stats[0] == 489 





