"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def screen():
    return Item("Монитор", 5000, 10)


def test_calculate_total_price(screen):
    assert screen.calculate_total_price() == 50000


def test_apply_discount(screen):
    Item.pay_rate = 0.5
    assert screen.apply_discount() is None
    assert screen.price == 2500
