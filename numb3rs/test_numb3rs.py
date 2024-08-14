from numb3rs import validate

def test_out_of_range():
    assert validate("253.254.255.256") == False

def test_not_formated():
    assert validate("1.2.3.4") == True
    assert validate("1.2.3") == False
    assert validate("1.2") == False
    assert validate("1") == False
    assert validate("cat") == False

def test_valid():
    assert validate("255.0.0.255") == True
