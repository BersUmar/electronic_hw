import csv
import pathlib


class InstantiateCSVError(Exception):
    def __init__(self, missing_column):
        self.missing_column = missing_column

    def __str__(self):
        return f'Отсутствует колонка {self.missing_column}'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__()
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

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __add__(self, other) -> int:
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    def __str__(self):
        return f'{self.__name}'

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        path = pathlib.Path(__file__).parent.joinpath('items.csv')
        try:
            with open(path, newline='', encoding='cp1251') as csvfile:
                reader: csv.DictReader = csv.DictReader(csvfile)
                for line in reader:
                    if not line["name"]:
                        raise InstantiateCSVError("name")
                    elif not line["price"]:
                        raise InstantiateCSVError("price")
                    elif not line["quantity"]:
                        raise InstantiateCSVError("quantity")
                    cls(line["name"], float(line["price"]), int(line["quantity"]))
        except FileNotFoundError as e:
            print(f'Ошибка выполнения : {e}')
        except InstantiateCSVError as er:
            print(er)

    @staticmethod
    def string_to_number(some: str):
        return int(float(some))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10 and name.isalpha():
            self.__name = name
        elif len(name) > 10 and name.isalpha():
            self.__name = name[0:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.pay_rate * self.price
