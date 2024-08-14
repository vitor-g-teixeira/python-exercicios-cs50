from datetime import date
import pytest
from seasons import get_date

def test_year_ago():
    year_ago = str(date.today())
    year_ago = year_ago.split("-")
    year_ago[0] = int(year_ago[0]) - 1
    assert get_date(str(year_ago[0]) + "-" + year_ago[1] + "-" + year_ago[2]) == "Five hundred twenty-five thousand, six hundred minutes"

def test_two_years_ago():
    two_years_ago = str(date.today())
    two_years_ago = two_years_ago.split("-")
    two_years_ago[0] = int(two_years_ago[0]) - 2
    assert get_date(str(two_years_ago[0]) + "-" + two_years_ago[1] + "-" + two_years_ago[2]) == "One million, fifty-one thousand, two hundred minutes"

def test_invalid():
    with pytest.raises(SystemExit):
        get_date("invalid")
