import pytest
import cli

def test_parsing_func(monkeypatch):
    monkeypatch.setattr("sys.argv", ["cli.py", "-r", "calendar_details.csv"])
    parser = cli.parsing_func()
    assert parser.nrows == "calendar_details.csv"
