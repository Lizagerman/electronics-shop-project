import csv
import os
from abc import ABC

path = os.path.join('..', 'src', 'items.csv')  # путь к файлу


class InstantiateCSVError(Exception):
    """Класс исключения при повреждении файла"""

    def __init__(self, name, message, base_message=None):
        self.name = name
        self.base_message = base_message
        self.message = message 

    def __str__(self):
        if self.base_message is None:
            return self.message

        return f'{self.message} - {str(self.base_message)}'


class TItem:
    pass


class Product:
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate: float = 1.0
    all: list[TItem] = []


    def __init__(self, name: str, price: int | float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)


    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        max_length: int = 10
        if len(value) > 10:
            raise Exception(f'Название не должно быть больше {max_length} символов')
        self.__name = value 

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity * self.pay_rate

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        :return:  Стоимость товара со скидкой.
        """
        self.price *= self.pay_rate
        return self.pay_rate

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return f"{__class__.__name__}('{str(self.__name)}', {str(self.price)}, {str(self.quantity)})"

    def __add__(self, other):
        temp = other.__class__.__name__  # имя другого класса (str)
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        else:
            return print("Складывать нельзя")


    if __name__ == ' __main__':
        product = Product(name, price, quantity)

# TestCase#1 name
    assert Product == 'Phone'

# TestCase#2 price
    product.price()
    assert 60000 * name.raise_coef == product.pay
    assert product.pay == 100000
