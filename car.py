# в модуле car создайте класс Car
# класс Car должен быть наследником Vehicle
from vehicle import Vehicle
from engine import Engine


class Car(Vehicle):
    DEFAULT_WEIGHT = 2500
    DEFAULT_FUEL = 70.0
    DEFAULT_FUEL_CONSUMPTION = 12.0

    def __init__(self, weight=DEFAULT_WEIGHT, fuel=DEFAULT_FUEL, fuel_consumption=DEFAULT_FUEL_CONSUMPTION):
        super().__init__(weight, fuel, fuel_consumption)
        self._engine = None

    # добавьте атрибут engine классу Car
    @property
    def engine(self):
        return self._engine

    # объявите метод set_engine, который принимает в себя экземпляр объекта Engine и устанавливает на текущий экземпляр Car
    def set_engine(self, engine: Engine):
        assert isinstance(engine, Engine)
        self._engine = engine