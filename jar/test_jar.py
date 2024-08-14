from jar import Jar
import pytest

def test_init():
    jar = Jar(5)
    assert jar.capacity == 5

def test_str():
    jar = Jar(5)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.capacity >= jar.size

    with pytest.raises(ValueError) as error:
        jar.deposit(8)

def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3

    with pytest.raises(ValueError)as error:
        jar.withdraw(8)
