# класс Plane должен быть наследником Vehicle
from exceptions import CargoOverload
from vehicle import Vehicle

class Plane(Vehicle):

    DEFAULT_WEIGHT = 50000
    DEFAULT_FUEL = 2000.0
    DEFAULT_FUEL_CONSUMPTION = 50.0

    # добавьте атрибуты cargo и max_cargo классу Plane
    # добавьте max_cargo в инициализатор (переопределите родительский)
    def __init__(self, max_cargo, weight=DEFAULT_WEIGHT, fuel=DEFAULT_FUEL, fuel_consumption=DEFAULT_FUEL_CONSUMPTION):
        super().__init__(weight, fuel, fuel_consumption)
        self._cargo = 0
        self._max_cargo = max_cargo

    @property
    def cargo(self):
        return self._cargo

    @property
    def max_cargo(self):
        return self._max_cargo

    # объявите метод load_cargo, который принимает число, проверяет, что в сумме с текущим cargo не будет перегруза, и обновляет значение, в ином случае выкидывает исключение exceptions. CargoOverload
    def load_cargo(self, added_cargo):
        common_cargo = self._cargo + added_cargo
        if common_cargo > self._max_cargo:
            raise CargoOverload
        else:
            self._cargo = common_cargo

    # объявите метод remove_all_cargo, который обнуляет значение cargo и возвращает значение cargo, которое было до обнуления.
    def remove_all_cargo(self):
        before_removing_cargo = self._cargo
        self._cargo = 0
        return before_removing_cargo