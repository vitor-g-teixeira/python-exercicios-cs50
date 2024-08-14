from fuel import convert, gauge
import pytest

def test_errors():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")
    for arg in ["random_text", "12/2"]:
        with pytest.raises(ValueError):
            convert(arg)

def test_ints():
    assert convert("1/3") == 33

def test_empty():
    assert gauge(1) == "E"
    assert gauge(1.1) != "E"

def test_fuel():
    assert gauge(99) == "F"
    assert gauge(98) != "F"

def test_normal():
    assert gauge(98) == "98%"
    assert gauge(2) == "2%"
