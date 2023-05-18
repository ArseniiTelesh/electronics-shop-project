import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price * Item.pay_rate
        self.quantity = quantity

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
        self.price = self.price * Item.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 10:
            self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls):
        with open('src/items.csv', newline='', encoding='windows-1251') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                name, price, quantity = row[0], float(row[1]), int(row[2])
                item = Item(name, price, quantity)
                Item.all.append(item)

    @staticmethod
    def string_to_number(string):
        if '.' in string:
            float_string = float(string)
            return int(float_string)
        return int(string)
