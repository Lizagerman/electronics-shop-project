import pytest

from src.keyboard import KeyBoard

kb = KeyBoard('Project KD87A', 9600, 5)


def test_keyboard_init():
    assert kb.name == 'Project KD87A'
    assert kb.price == 9600
    assert kb.quantity == 5
    assert kb.language == 'EN'


def test_language():
    kb.change_lang()
    assert str(kb.language) == 'RU'


def test_change_lang():
    kb.change_lang().change_lang()

    assert str(kb.language) == 'RU'


def test_other_language():
    with pytest.raises(AttributeError):
        kb.language = 'CH'
