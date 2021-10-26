from abc import ABC, abstractmethod
from exceptions import exceptions_transport as Ex
from base_transport import BaseTransport
from helper import Helpers


# Base abstract
class PassengerCar(BaseTransport):
    local_type = 'Land'
    carrying_capacity = None

    def __init__(self, name, seat, transmission):
        self.name = name
        self.seat = seat
        self.transmission = transmission

    def __add__(self, other):
        return BaseTransport('summ seats:', self.seat + other.seat)

    def __str__(self):
        return f'{self.name} ({self.local_type}), seats:  {self.seat}, transmission  - {self.transmission}'

    def __repr__(self):
        return f'{self.name} ({self.local_type}), seats:  {self.seat}, transmission  - {self.transmission}'

    @abstractmethod
    def make_sound():
        pass

    @property
    def carrying_capacity(self):
        return self.carrying_capacity

    @carrying_capacity.setter
    def carrying_capacity(self, carrying_capacity):
        self.carrying_capacity = carrying_capacity

    def calc_carrying_capacity(self):
        if self.seat:
            self.carrying_capacity = self.seat * 80
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
            raise Ex.MovingException('The doors are not closed !')
        if self.fasten_belts is not True:
            raise Ex.MovingException('Belts not fastened !')
        if self.start_engine is not True:
            raise Ex.MovingException('Engine not running !')

        print('Moving.')


class PassengerBoat(BaseTransport):
    local_type = 'Water'
    carrying_capacity = None

    def __init__(self, name, seat, draft):
        self.name = draft
        self.seat = draft
        self.draft = draft

    def __add__(self, other):
        return BaseTransport('summ seats:', self.seat + other.seat)

    def __str__(self):
        return f'{self.name} ({self.local_type}), seats:  {self.seat}, draft  - {self.draft}'

    def __repr__(self):
        return f'{self.name} ({self.local_type}), seats:  {self.seat}, draft  - {self.draft}'

    def raise_anchor(self):
        self.raise_anchor = True

    def start_engine(self):
        self.start_engine = True

    def start_moving(self):
        if self.raise_anchor != True:
            raise Ex.MovingException('Anchor not raised !')
        if self.start_engine != True:
            raise Ex.MovingException('Engine not running !')

        print('Moving.')


class PassengerPlane(BaseTransport):
    local_type = 'Air'
    carrying_capacity = None

    def make_sound(self):
        return 'Wuuuuuuuu'

    def carrying_capacity(self):
        return self.carrying_capacity

    def close_dors(self):
        self.close_dors = True

    def fasten_belts(self):
        self.fasten_belts = True

    def start_engine(self):
        self.start_engine = True

    def start_moving(self):
        if self.close_dors != True:
            raise Ex.MovingException('The doors are not closed !')
        if self.fasten_belts != True:
            raise Ex.MovingException('Belts not fastened !')
        if self.start_engine != True:
            raise Ex.MovingException('Engine not running !')

        print('Moving.')

    @staticmethod
    def calculate_bagage_weith(bagage_weith, total_passager):
        return bagage_weith * total_passager;
