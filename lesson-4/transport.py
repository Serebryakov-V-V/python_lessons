from sub_transport import PassengerBoat, PassengerCar, PassengerPlane, CarryCapacityMixin
from exceptions import exceptions_transport as Ex


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
class Сrossover(PassengerCar, CarryCapacityMixin):
    local_type = 'Сrossover'

    def __init__(self, name, seat, transmission, climat_cintroll_zone):
        super().__init__(name, seat, transmission)
        self.climat_cintroll_zone = climat_cintroll_zone

    def __repr__(self):
        return f'{self.name} ({self.local_type}),' f'seats:  {self.seat}, transmission  - {self.transmission},' f' Climat zone: {self.climat_cintroll_zone}'

    def __str__(self):
        return f'{self.name} ({self.local_type}),' f' seats:  {self.seat}, transmission  - {self.transmission},' f' Climat zone: {self.climat_cintroll_zone}'

    @staticmethod
    def caclc_power_reserve(fuel_consumption, fuel_remaining, fuel_type='petrol'):
        if fuel_type == 'petrol':
            try:
                return (100 / fuel_consumption) * fuel_remaining
            except ZeroDivisionError:
                return 10;
        else:
            raise ValueError('Error fuel_type is not "petrol"')

    def power_reserve(self):
        return self.caclc_power_reserve(self.fuel_consumption, self.fuel_remaining, 'petrol')
