# доработайте базовый класс base. Vehicle:
from abc import ABC
from exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):


    # добавьте атрибуты weight, started, fuel, fuel_consumption со значениями по умолчанию
    # добавьте инициализатор для установки weight, fuel, fuel_consumption
    # и обновляет состояние started, иначе выкидывает исключение exceptions.LowFuelError
    DEFAULT_WEIGHT = 2000
    DEFAULT_FUEL = 45.0
    DEFAULT_FUEL_CONSUMPTION = 15.0

    def __init__(self, weight=DEFAULT_WEIGHT, fuel=DEFAULT_FUEL, fuel_consumption=DEFAULT_FUEL_CONSUMPTION):
        self._weight = weight
        self._fuel = fuel
        self._fuel_consumption = fuel_consumption
        if self.fuel > 0.0:
            self._started = True
        else:
            raise LowFuelError

    @property
    def weight(self):
        return self._weight

    @property
    def fuel(self):
        return self._fuel

    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    @property
    def started(self):
        return self._started

    @started.setter
    def started(self, value):
        self._started = value

    # добавьте метод move, который проверяет, что достаточно топлива для преодоления переданной дистанции,
    # и изменяет количество оставшегося топлива, иначе выкидывает исключение exceptions. NotEnoughFuel
    def move(self, distance):
        if self._fuel_consumption>0 :
            required_fuel = distance/self._fuel_consumption
            if self._fuel >= required_fuel:
                self._fuel -= required_fuel
            else:
                raise NotEnoughFuel
        else:
            raise NotEnoughFuel

