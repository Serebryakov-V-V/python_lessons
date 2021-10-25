from sub_transport import PassengerBoat, PassengerCar, PassengerPlane
from exceptions import exceptions_transport as Ex
from helper import Helpers


class Trasporters:

    def __init__(self):
        self.items = []

    def total_capacity(self):
        return sum(el.seat for el in self.items)

    def __iadd__(self, other):
        self.items.append(other)
        return self

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return (el for el in self.items)


# Child base abstract
class Сrossover(PassengerCar):
    local_type = 'Сrossover'

    def __init__(self, name, seat, transmission, climat_cintroll_zone):
        super().__init__(name, seat, transmission)
        self.climat_cintroll_zone = climat_cintroll_zone

    def __repr__(self):
        return f'{self.name} ({self.local_type}), seats:  {self.seat}, transmission  - {self.transmission}, Climat zone: {self.climat_cintroll_zone}'

    def __str__(self):
        return f'{self.name} ({self.local_type}), seats:  {self.seat}, transmission  - {self.transmission}, Climat zone: {self.climat_cintroll_zone}'

    @property
    def carrying_capacity(self):
        if Helpers.check_empty(self.seat):
            return self.carrying_capacity
        raise Ex.SeatsValueException('Empty seat value.')

    @staticmethod
    def caclc_power_reserve(fuel_consumption, fuel_remaining):
        return (100 / fuel_consumption) * fuel_remaining
