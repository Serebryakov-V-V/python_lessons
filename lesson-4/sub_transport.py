from abc import ABC, abstractmethod
from exceptions import exceptions_transport as ex
from base_transport import BaseTransport
from helper import Helpers


# Base abstract
class PassengerCar(BaseTransport):
    local_type = 'Land'
    _carrying_capacity = None

    def __init__(self, name, seat, transmission):
        self.name = name
        self.seat = seat
        self.transmission = transmission

    def __add__(self, other):
        return BaseTransport('summ seats:', self.seat + other.seat)

    def __str__(self):
        return f'{self.name} ({self.local_type}),' f'seats:  {self.seat}, transmission  - {self.transmission}'

    def __repr__(self):
        return f'{self.name} ({self.local_type}),' f' seats:  {self.seat}, transmission  - {self.transmission}'

    def __iter__(self):
        return (el for el in self.items)


    @staticmethod
    def make_sound():
        print('Bebeee')

    @property
    def carrying_capacity(self):
        return self._carrying_capacity

    @carrying_capacity.setter
    def carrying_capacity(self, carrying_capacity):
        self._carrying_capacity = carrying_capacity

    def calc_carrying_capacity(self):
        if self.seat:
            self._carrying_capacity = self.seat * 80
        else:
            raise ValueError('Incorrect seat value.')

    def close_dors(self):
        self.close_dors = True

    def fasten_belts(self):
        self.fasten_belts = True

    def start_engine(self):
        self.start_engine = True

    def start_moving(self):
        if self.close_dors is not True:
            raise ex.MovingException('The doors are not closed !')
        if self.fasten_belts is not True:
            raise ex.MovingException('Belts not fastened !')
        if self.start_engine is not True:
            raise ex.MovingException('Engine not running !')

        print('Moving.')


class PassengerBoat(BaseTransport):
    local_type = 'Water'
    _carrying_capacity = None

    def __init__(self, name, seat, draft):
        self.name = name
        self.seat = seat
        self.draft = draft

    def __add__(self, other):
        return BaseTransport('summ seats:', self.seat + other.seat)

    def __str__(self):
        return f'{self.name} ({self.local_type}),' f' seats:  {self.seat}, draft  - {self.draft}'

    def __repr__(self):
        return f'{self.name} ({self.local_type}),' f' seats:  {self.seat}, draft  - {self.draft}'

    def __iter__(self):
        return (el for el in self.items)

    @property
    def carrying_capacity(self):
        return self._carrying_capacity

    @carrying_capacity.setter
    def carrying_capacity(self, carrying_capacity):
        self._carrying_capacity = carrying_capacity

    def calc_carrying_capacity(self):
        if self.seat:
            self._carrying_capacity = self.seat * 80
        else:
            raise ValueError('Incorrect seat value.')

    def raise_anchor(self):
        self.raise_anchor = True

    def start_engine(self):
        self.start_engine = True

    def start_moving(self):
        if self.raise_anchor != True:
            raise ex.MovingException('Anchor not raised !')
        if self.start_engine != True:
            raise ex.MovingException('Engine not running !')

        print('Moving.')


class PassengerPlane(BaseTransport):
    local_type = 'Air'
    _carrying_capacity = None


    def __init__(self, name, seat, staff):
        self.name = name
        self.seat = seat
        self.staff = staff

    def __add__(self, other):
        return BaseTransport('summ seats:', self.seat + other.seat)

    def __str__(self):
        return f'{self.name} ({self.local_type}),' f' seats:  {self.seat},' f' Personal on board  - {self.staff}'

    def __repr__(self):
        return f'{self.name} ({self.local_type}),' f' seats:  {self.seat},' f' Personal on board  - {self.staff}'

    def __iter__(self):
        return (el for el in self.items)

    @property
    def carrying_capacity(self):
        return self._carrying_capacity

    @carrying_capacity.setter
    def carrying_capacity(self, carrying_capacity):
        self._carrying_capacity = carrying_capacity

    def calc_carrying_capacity(self):
        if self.seat:
            self._carrying_capacity = self.seat * 80
        else:
            raise ValueError('Incorrect seat value.')

    def close_dors(self):
        self.close_dors = True

    def fasten_belts(self):
        self.fasten_belts = True

    def start_engine(self):
        self.start_engine = True

    def start_moving(self):
        if self.close_dors != True:
            raise ex.MovingException('The doors are not closed !')
        if self.fasten_belts != True:
            raise ex.MovingException('Belts not fastened !')
        if self.start_engine != True:
            raise ex.MovingException('Engine not running !')

        print('Moving.')

    @staticmethod
    def calculate_bagage_weith(bagage_weith, total_passager):
        return bagage_weith * total_passager;
