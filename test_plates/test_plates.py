from plates import is_valid

def test_length():
    assert is_valid("s") == False
    assert is_valid("toolong") == False

def test_beggining():
     assert is_valid("CS50") == True
     assert is_valid("C550") == False

def test_invalid_characteres():
    assert is_valid("CS50_") == False

def test_numbers():
    assert is_valid("CS05") == False
    assert is_valid("CS50C") == False
