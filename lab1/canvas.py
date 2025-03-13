from figure import Figure

class Canvas:
    def __init__(self, width: int = 100, height: int = 40) -> None:
        self.width = width
        self.height = height
        self._figures = []
        self._grid = [[' ' for _ in range(width)] for _ in range(height)]

    def add_figure(self, figure: Figure) -> None:
        self._figures.append(figure)

    def remove_figure(self, index: int) -> None:
        if 0 <= index < len(self._figures):
            del self._figures[index]

    def draw(self) -> None:
        # Очищаем холст
        self._grid = [[' ' for _ in range(self.width)] for _ in range(self.height)]

        # Рисуем фигуры
        for figure in self._figures:
            figure.draw(self)

        # Отображаем холст
        for row in self._grid:
            print(''.join(row))

    def toggle_fill(self, index: int) -> None:
        if 0 <= index < len(self._figures):
            self._figures[index].filled = not self._figures[index].filled
