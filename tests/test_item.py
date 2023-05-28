"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def screen():
    return Item("Монитор", 5000, 10)


def test___repr__(screen):
    assert repr(screen) == "Item('Монитор', 5000, 10)"


def test___str__(screen):
    assert str(screen) == 'Монитор'


def test___add__(screen):
    phone = Phone('Nokia3320', 500, 2, 1)
    assert screen + phone == 12


def test_name():
    screen = Item("Монитор", 5000, 10)
    assert screen.name == 'Монитор'
    screen.name = 'Samsung'
    assert screen.name == 'Samsung'
    screen.name = 'Большой_Монитор'
    assert screen.name != 'Большой_Монитор'


def test_calculate_total_price(screen):
    assert screen.calculate_total_price() == 50000


def test_apply_discount(screen):
    Item.pay_rate = 0.5
    assert screen.apply_discount() is None
    assert screen.price == 2500


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('14.99') == 14
    assert Item.string_to_number('12') == 12
