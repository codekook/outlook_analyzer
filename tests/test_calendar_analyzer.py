import calendar_analyzer
from unittest.mock import patch 

def test_main_time_stats(monkeypatch, capsys):

    """Tests the end to end funcationality of running the application to return"""

    monkeypatch.setattr("sys.argv", ["calendar_analyzer.py", "-s", "calendar_details.csv"])
    calendar_analyzer.main()
    output = capsys.readouterr().out.rstrip()
    assert output == "stats(count=489, errors=0, sum=56830.0, min=5.0, max=540.0, mean=116.21676891615543, pvariance=21478.42744886478, pstdev=146.55520273557258)"

def test_main_quickview(monkeypatch, capsys):

    """Tests the end to end functionality of running the application to return the number of rows in a table"""

    monkeypatch.setattr("sys.argv", ["calendar_analyzer.py", "-r", "calendar_details.csv"])
    calendar_analyzer.main()
    with patch('builtins.input', return_value=5):
        output = capsys.readouterr().out.rstrip()
    assert output == "file rows: 489"