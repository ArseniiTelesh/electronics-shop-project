import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def phone():
    return Phone('Iphone XL', 1000, 15, 2)


def test___repr__(phone):
    assert repr(phone) == "Phone('Iphone XL', 1000, 15, 2)"


def test___add__(phone):
    item = Item("Монитор", 5000, 10)
    assert phone + item == 25


def test_number_of_sim(phone):
    assert phone.number_of_sim == 2
    phone.number_of_sim = 1
    assert phone.number_of_sim == 1
    phone.number_of_sim = 3.3
    assert phone.number_of_sim == 3.3
    phone.number_of_sim = 0
    assert phone.number_of_sim != 1
