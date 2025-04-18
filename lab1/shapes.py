from figure import Figure

class Rectangle(Figure):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        super().__init__(x, y)
        self._width = width
        self._height = height

    def draw(self, canvas) -> None:
        for i in range(self._height):
            for j in range(self._width):
                cx = self._x + j
                cy = self._y + i
                if 0 <= cx < canvas.width and 0 <= cy < canvas.height:
                    if self.filled and 0 < i < self._height - 1 and 0 < j < self._width - 1:
                        canvas._grid[cy][cx] = 'x'  # Символ для заливки
                    elif i == 0 or i == self._height - 1 or j == 0 or j == self._width - 1:
                        canvas._grid[cy][cx] = '#'  # Символ рамки

    def fill(self, canvas) -> None:
        if self.filled:
            for i in range(1, self._height - 1):
                for j in range(1, self._width - 1):
                    cx = self._x + j
                    cy = self._y + i
                    if 0 <= cx < canvas.width and 0 <= cy < canvas.height:
                        canvas._grid[cy][cx] = 'x'  # Символ для заливки


class Circle(Figure):
    def __init__(self, x: int, y: int, radius: int) -> None:
        super().__init__(x, y)
        self._radius = radius

    def draw(self, canvas) -> None:
        r = self._radius
        for i in range(-r, r + 1):
            for j in range(-r, r + 1):
                cx = self._x + j
                cy = self._y + i
                if 0 <= cx < canvas.width and 0 <= cy < canvas.height:
                    if self.filled and i**2 + j**2 < r**2:
                        canvas._grid[cy][cx] = 'x'  # Символ для заливки
                    elif i**2 + j**2 == r**2:
                        canvas._grid[cy][cx] = 'O'  # Символ рамки

    def fill(self, canvas) -> None:
        if self.filled:
            r = self._radius
            for i in range(-r, r + 1):
                for j in range(-r, r + 1):
                    if i**2 + j**2 < r**2:
                        cx = self._x + j
                        cy = self._y + i
                        if 0 <= cx < canvas.width and 0 <= cy < canvas.height:
                            canvas._grid[cy][cx] = 'x'  # Символ для заливки


class Triangle(Figure):
    def __init__(self, x: int, y: int, a: int, b: int, c: int) -> None:
        super().__init__(x, y)
        self._a = a
        self._b = b
        self._c = c

    def draw(self, canvas) -> None:
        # Рисуем рамки
        self._draw_line(canvas, self._x, self._y, self._x + self._b, self._y, '^')  # Нижняя сторона
        self._draw_line(canvas, self._x, self._y, self._x + self._a // 2, self._y - self._c, '^')  # Левая сторона
        self._draw_line(canvas, self._x + self._b, self._y, self._x + self._a // 2, self._y - self._c, '^')  # Правая сторона

        if self.filled:
            # Заполняем треугольник
            for y in range(self._y - self._c + 1, self._y + 1):
                for x in range(self._x, self._x + self._b + 1):
                    if 0 <= y < canvas.height and 0 <= x < canvas.width:
                        if self._is_inside_triangle(x, y):
                            canvas._grid[y][x] = 'x'  # Символ для заливки

    def fill(self, canvas) -> None:
        if self.filled:
            # Заполняем треугольник
            for y in range(self._y - self._c + 1, self._y + 1):
                for x in range(self._x, self._x + self._b + 1):
                    if 0 <= y < canvas.height and 0 <= x < canvas.width:
                        if self._is_inside_triangle(x, y):
                            canvas._grid[y][x] = 'x'  # Символ для заливки

    def _draw_line(self, canvas, x1, y1, x2, y2, symbol):
        dx = x2 - x1
        dy = y2 - y1
        steps = max(abs(dx), abs(dy))
        if steps == 0:
            return

        x_increment = dx / steps
        y_increment = dy / steps
        x = x1
        y = y1

        for _ in range(steps + 1):
            if 0 <= int(y) < canvas.height and 0 <= int(x) < canvas.width:
                canvas._grid[int(y)][int(x)] = symbol
            x += x_increment
            y += y_increment

    def _is_inside_triangle(self, x: int, y: int) -> bool:
        # Проверка, находится ли точка (x, y) внутри треугольника
        x1, y1 = self._x + self._b / 2, self._y - self._c  # Верхняя вершина
        x2, y2 = self._x, self._y  # Левая вершина
        x3, y3 = self._x + self._b, self._y  # Правая вершина

        # Используем барицентрические координаты
        d1 = (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1)
        d2 = (x3 - x2) * (y - y2) - (y3 - y2) * (x - x2)
        d3 = (x1 - x3) * (y - y3) - (y1 - y3) * (x - x3)

        has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
        has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

        return not (has_neg and has_pos)  # Если все положительные или все отрицательные
