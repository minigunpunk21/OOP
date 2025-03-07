import copy
import os
from shapes import Rectangle, Circle, Triangle

class Canvas:
    def __init__(self, width: int = 80, height: int = 25) -> None:
        self._width = width
        self._height = height
        self._figures = []
        self._history = []
        self._redo_stack = []
        self._create_grid()

    def _create_grid(self) -> None:
        self._grid = [[" " for _ in range(self._width)] for _ in range(self._height)]

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @property
    def figures(self):
        return self._figures

    def _save_state(self) -> None:
        self._history.append(copy.deepcopy(self._figures))
        self._redo_stack.clear()

    def add_figure(self, figure) -> None:
        self._save_state()
        self._figures.append(figure)

    def remove_figure(self, index: int) -> None:
        if 0 <= index < len(self._figures):
            self._save_state()
            del self._figures[index]

    def move_figure(self, index: int, dx: int, dy: int) -> None:
        if 0 <= index < len(self._figures):
            self._save_state()
            self._figures[index].move(dx, dy)

    def undo(self) -> None:
        if self._history:
            self._redo_stack.append(copy.deepcopy(self._figures))
            self._figures = self._history.pop()

    def redo(self) -> None:
        if self._redo_stack:
            self._history.append(copy.deepcopy(self._figures))
            self._figures = self._redo_stack.pop()

    def draw(self) -> None:
        self._create_grid()
        for figure in self._figures:
            figure.draw(self)
        os.system("cls" if os.name == "nt" else "clear")
        self._print_grid()

    def _print_grid(self) -> None:
        for row in self._grid:
            print("".join(row))

