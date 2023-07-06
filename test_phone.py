import pytest

from src.phone import Phone


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_phone_init(phone1):
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120_000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2
    with pytest.raises(ValueError, match='Количество физических SIM-карт должно быть целым числом больше нуля.'):
        phone1.number_of_sim = 0


def test_number_of_sim(phone1):
    phone1.number_of_sim = 2
    assert phone1.number_of_sim == 2
    with pytest.raises(ValueError, match='Количество физических SIM-карт должно быть целым числом больше нуля.'):
        phone1.number_of_sim = 0


def test_phone_str(phone1):
    assert phone1.__str__() == "iPhone 14"


def test_phone_repr(phone1):
    assert phone1.__repr__() == "Phone('iPhone 14', 120000, 5, 2)"
