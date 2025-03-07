from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int) -> None:
        self._x = value

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int) -> None:
        self._y = value

    @abstractmethod
    def draw(self, canvas) -> None:
        pass

    def move(self, dx: int, dy: int) -> None:
        self._x += dx
        self._y += dy
