import cli

def test_parsing_func_nrows(monkeypatch):

    """Tests the parser's ability to accept the nrows argument"""

    monkeypatch.setattr("sys.argv", ["cli.py", "-r", "calendar_details.csv"])
    parser = cli.parsing_func()
    assert parser.nrows == "calendar_details.csv"

def test_parsing_func_monthly_activity(monkeypatch):

    """Tests the parser's ability to accept the monthly_activity argument"""

    monkeypatch.setattr("sys.argv", ["cli.py", "-ma", "calendar_details.csv"])
    parser = cli.parsing_func()
    assert parser.monthly_activity == "calendar_details.csv"

def test_parsing_func_time_stats(monkeypatch):

    """Tests the parser's ability to accept the time_stats argument"""

    monkeypatch.setattr("sys.argv", ["cli.py", "-s", "calendar_details.csv"])
    parser = cli.parsing_func()
    assert parser.time_stats == "calendar_details.csv"

def test_parsing_func_quickview(monkeypatch):

    """Tests the parser's ability to accept the quickview argument"""

    monkeypatch.setattr("sys.argv", ["cli.py", "-q", "calendar_details.csv"])
    parser = cli.parsing_func()
    assert parser.quickview == "calendar_details.csv"
