from abc import ABC, abstractmethod
from exceptions import exceptions_transport as Ex


# Meta class
class BaseTransport(ABC):

    @property
    def carrying_capacity(self):
        raise NotImplementedError('Property "carrying_capacity" not defined.')

    @carrying_capacity.setter
    def carrying_capacity(self):
        raise NotImplementedError('Setter "carrying_capacity" not defined.')

    def calc_carrying_capacity(self):
       raise NotImplementedError('Method "calc_carrying_capacity" not defined.')

    def set_seat(self, seat):
        raise NotImplementedError('Method "set_seat" not defined.')

    @abstractmethod
    def start_moving(self):
        pass
