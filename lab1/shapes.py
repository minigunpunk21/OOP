from figure import Figure

class Rectangle(Figure):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        super().__init__(x, y)
        self._width = width
        self._height = height

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def draw(self, canvas) -> None:
        for i in range(self._height):
            for j in range(self._width):
                cx = self._x + j
                cy = self._y + i
                if 0 <= cx < canvas.width and 0 <= cy < canvas.height:
                    canvas._grid[cy][cx] = '#'

class Circle(Figure):
    def __init__(self, x: int, y: int, radius: int) -> None:
        super().__init__(x, y)
        self._radius = radius

    @property
    def radius(self) -> int:
        return self._radius

    def draw(self, canvas) -> None:
        r = self._radius
        for i in range(-r, r + 1):
            for j in range(-r, r + 1):
                if i**2 + j**2 <= r**2:
                    cx = self._x + j
                    cy = self._y + i
                    if 0 <= cx < canvas.width and 0 <= cy < canvas.height:
                        canvas._grid[cy][cx] = 'O'

class Triangle(Figure):
    def __init__(self, x: int, y: int, base: int, height: int) -> None:
        super().__init__(x, y)
        self._base = base
        self._height = height

    @property
    def base(self) -> int:
        return self._base

    @property
    def height(self) -> int:
        return self._height

    def draw(self, canvas) -> None:
        for i in range(self._height):
            if i == self._height - 1:
                fill_count = self._base
            else:
                fill_count = int(((i + 1) * self._base) / self._height)
                fill_count = max(fill_count, 1)
            left_offset = (self._base - fill_count) // 2
            for j in range(fill_count):
                cx = self._x + left_offset + j
                cy = self._y + i
                if 0 <= cx < canvas.width and 0 <= cy < canvas.height:
                    canvas._grid[cy][cx] = '*'

