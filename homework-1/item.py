import csv
import os
from abc import ABC

path = os.path.join('..', 'src', 'items.csv')  # путь к файлу


class InstantiateCSVError(Exception):

    def __init__(self, message, base_message=None):
        self.base_message = base_message
        self.message = message

    def __str__(self):
        if self.base_message is None:
            return self.message

        return f'{self.message} - {str(self.base_message)}'


class Item(ABC):

    pay_rate = 1.
    all = []

    # path = os.path.join('..', 'electronics-shop-project_AV', 'scr', 'items.csv')

    def __init__(self, name: str, price: float, quantity: int) -> None:

        self.verify_name(name)

        self.__name = name
        self.price = price
        self.quantity = quantity
        super().__init__()

    @classmethod
    def verify_name(cls, name):
        if len(name) >= 15:
            raise Exception("Длина наименования товара превышает 10 символов.")

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        try:
            with open(path, encoding='windows-1251', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                cls.all = [cls((row['name']), float(row['price']), int(row['quantity'])) for row in reader]

        except FileNotFoundError:
            print('_Отсутствует файл item.csv_')

        except KeyError as e:
            print(InstantiateCSVError("_Файл item.csv поврежден_", e))
        print(cls.all)
        return cls.all

    @staticmethod
    def string_to_number(str_number):
        return int(float(str_number))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.verify_name(name)
        self.__name = name

    def calculate_total_price(self) -> float:

        return self.price * self.quantity * self.pay_rate

    def apply_discount(self) -> float:

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

