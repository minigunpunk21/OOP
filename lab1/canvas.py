import copy
from figure import Figure

class Canvas:
    def __init__(self, width: int = 100, height: int = 40) -> None:
        self.width = width
        self.height = height
        self._figures = []
        self._grid = [[' ' for _ in range(width)] for _ in range(height)]
        self._undo_stack = []  # Стек для undo
        self._redo_stack = []  # Стек для redo

    def save_state(self):
        # Сохраняем глубокую копию списка фигур и очищаем redo-стек
        self._undo_stack.append(copy.deepcopy(self._figures))
        self._redo_stack.clear()

    def add_figure(self, figure: Figure) -> None:
        self.save_state()  # Сохраняем состояние перед изменением
        self._figures.append(figure)

    def remove_figure(self, index: int) -> None:
        if 0 <= index < len(self._figures):
            self.save_state()
            del self._figures[index]

    def toggle_fill(self, index: int) -> None:
        if 0 <= index < len(self._figures):
            self.save_state()
            self._figures[index].filled = not self._figures[index].filled

    def move_figure(self, index: int, new_x: int, new_y: int) -> None:
        if 0 <= index < len(self._figures):
            self.save_state()
            self._figures[index].move(new_x, new_y)

    def undo(self) -> None:
        if self._undo_stack:
            # Сохраняем текущее состояние в redo-стек, затем восстанавливаем предыдущее состояние
            self._redo_stack.append(copy.deepcopy(self._figures))
            self._figures = self._undo_stack.pop()
        else:
            print("Nothing to undo.")

    def redo(self) -> None:
        if self._redo_stack:
            self._undo_stack.append(copy.deepcopy(self._figures))
            self._figures = self._redo_stack.pop()
        else:
            print("Nothing to redo.")

    def draw(self) -> None:
        # Очищаем холст
        self._grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        # Рисуем все фигуры
        for figure in self._figures:
            figure.draw(self)
        # Выводим холст в консоль
        for row in self._grid:
            print(''.join(row))

