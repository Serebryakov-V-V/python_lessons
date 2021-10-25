from abc import ABC, abstractmethod
from exceptions import exceptions_transport as Ex


# Meta class
class BaseTransport(ABC):
    local_type = None
    carrying_capacity = None

    def __init__(self, name, seat):
        self.name = name
        self.seat = seat

    def __str__(self):
        return f'{self.name} ({self.local_type}), seats:  {self.seat}'

    def __add__(self, other):
        return BaseTransport('summ seats:', self.seat + other.seat)

    @property
    def carrying_capacity(self):
        return self.carrying_capacity

    @carrying_capacity.setter
    def carrying_capacity(self):
        if self.seat:
            self.carrying_capacity = 80 * self.seat
        else:
            raise Ex.SeatsValueException('Seat is empty.')

    def set_seat(self, seat):
        self.seat = seat

    @abstractmethod
    def start_moving(self):
        pass
