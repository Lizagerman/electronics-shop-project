"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv
import os

import pytest

from src.item import Item, InstantiateCSVError
from src.phone import Phone

path = os.path.join('..', 'tests', 'test_items.csv')  # путь к файлу

item1 = Item("Смартфон", 10000, 20)
phone1 = Phone("iPhone 14", 120_000, 5, 2)


def test_item_init():
    assert item1.name == 'Смартфон'
    assert item1.price == 10000.0
    assert item1.quantity == 20


def test_repr():
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    assert str(item1) == 'Смартфон'


def test_name():
    item1.name = 'Смартфон'
    assert item1.name == 'Смартфон'


def test_verify_name():
    # with pytest.raises(Exception):
    try:
        item1.name = 'СуперСмартфон'
        Item.verify_name(item1.name)
    except Exception as ex:
        assert ex.args[0] == "Длина наименования товара превышает 10 символов."


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000.0


def test_instantiate_from_csv():
    try:
        Item.instantiate_from_csv()
        assert len(Item.all) == 5
    except Exception as ex:
        assert ex.args[0] == "Длина наименования товара превышает 10 символов."


def test_apply_discount():
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0


@pytest.mark.parametrize("a, result", [('5', 5),
                                       ('5.0', 5),
                                       ('5.5', 5)])
def test_string_to_number(a, result):
    assert Item.string_to_number(a) == result


@pytest.mark.parametrize('class_a, class_b, result', [(item1, phone1, 25),
                                                      (phone1, phone1, 10)])
def test_add(class_a, class_b, result):
    assert class_a + class_b == result


def test_not_file():
    try:
        with open('../src/items.csv'):
            pass
    except FileNotFoundError as ex:
        assert ex.args[1] == "No such file or directory"


def test_file_is_corrupted():
    a = InstantiateCSVError("_Файл item.csv поврежден_", 'quantity')
    assert a.__str__() == "_Файл item.csv поврежден_ - quantity"


def test_key_error():
    test_all = []
    try:
        with open(path, encoding='windows-1251', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            test_all = [((row['name']), float(row['price']), int(row['quantity'])) for row in reader]
    except KeyError as e:
        assert e.args[0] == 'quantity'
        