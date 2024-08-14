from bank import value

def test_h():
    assert value("HELLO, friend") == 0
    assert value("hello, friend") == 0
    assert value("how are you") == 20
    assert value("Hey") == 20

def test_non_h():
    assert value("non h") == 100
