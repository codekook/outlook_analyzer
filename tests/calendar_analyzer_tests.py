import pytest 
import calendar_analyzer

def test_main(argument_parser):
    assert argument_parser == "calendar_details.csv"