import calendar_analyzer

def test_main_time_stats(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["calendar_analyzer.py", "-s", "calendar_details.csv"])
    calendar_analyzer.main()
    output = capsys.readouterr().out.rstrip()
    assert output == "stats(count=489, errors=0, sum=56830.0, min=5.0, max=540.0, mean=116.21676891615543, pvariance=21478.42744886478, pstdev=146.55520273557258)"

def test_main_quickview(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["calendar_analyzer.py", "-r", "calendar_details.csv"])
    calendar_analyzer.main()
    output = capsys.readouterr().out.rstrip()
    assert output == "file rows: 489"