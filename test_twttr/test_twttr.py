from twttr import shorten

def test_upper_alphabet():
    assert shorten("1. ABCDEFGHIJKLMONPQRSTUVWXYZ") == "1. BCDFGHJKLMNPQRSTVWXYZ"

def test_lower_alphabet():
    assert shorten("1. abcdefghijklmnopqrstuvwxyz") == "1. bcdfghjklmnpqrstvwxyz"
