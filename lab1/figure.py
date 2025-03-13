from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y
        self._filled = False  # По умолчанию фигура не заполнена

    @property
    def filled(self):
        return self._filled

    @filled.setter
    def filled(self, value: bool):
        self._filled = value

    @abstractmethod
    def draw(self, canvas) -> None:
        pass

    @abstractmethod
    def fill(self, canvas) -> None:
        pass

    def move(self, new_x: int, new_y: int) -> None:
        self._x = new_x
        self._y = new_y
