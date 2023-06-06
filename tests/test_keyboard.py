import pytest
from src.keyboard import Keyboard


@pytest.fixture()
def keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_language(keyboard):
    assert keyboard.language == 'EN'


def test_change_lang(keyboard):
    keyboard.change_lang()
    assert str(keyboard.language) == "RU"

    keyboard.change_lang().change_lang()
    assert str(keyboard.language) == "RU"
