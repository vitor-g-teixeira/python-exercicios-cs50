from um import count

def test_um():
    assert count("um") == 1

def test_space():
    assert count("umum") == 0
    assert count("um um") == 2

def test_uminword():
    assert count("yum") == 0

def test_um_caseinsensitive():
    assert count("um, Um, uM, UM...") == 4
