from src.item import Item


class Phone(Item):

    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self._number_of_sim})"

    def __add__(self, other):
        if other == Item or Phone:
            return self.quantity + other.quantity
        else:
            raise TypeError('Можно складывать только классы Phone и Item')

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number):
        if new_number == 0 or isinstance(new_number, float):
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self._number_of_sim = new_number
