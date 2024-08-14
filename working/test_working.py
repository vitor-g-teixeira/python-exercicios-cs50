from working import convert
import pytest

def test_invalid():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

def test_out_range():
    with pytest.raises(ValueError):
        convert("13:00 AM to 14:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60")

def test_valid():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
