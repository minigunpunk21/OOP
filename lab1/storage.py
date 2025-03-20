import json
from shapes import Rectangle, Circle, Triangle

class Storage:
    @staticmethod
    def save(canvas, filename: str) -> None:
        data = []
        for figure in canvas._figures:
            # Use a dictionary to clearly define what to save
            if isinstance(figure, Rectangle):
                d = {
                    '_type': 'Rectangle',
                    'x': figure._x,
                    'y': figure._y,
                    'width': figure._width,
                    'height': figure._height,
                    'filled': figure.filled
                }
            elif isinstance(figure, Circle):
                d = {
                    '_type': 'Circle',
                    'x': figure._x,
                    'y': figure._y,
                    'radius': figure._radius,
                    'filled': figure.filled
                }
            elif isinstance(figure, Triangle):
                d = {
                    '_type': 'Triangle',
                    'x': figure._x,
                    'y': figure._y,
                    'a': figure._a,
                    'b': figure._b,
                    'c': figure._c,
                    'filled': figure.filled
                }
            data.append(d)
        with open(filename, 'w') as f:
            json.dump(data, f)

    @staticmethod
    def load(filename: str):
        figures = []
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for item in data:
                    ftype = item.pop('_type', None)
                    if ftype == 'Rectangle':
                        figures.append(Rectangle(item['x'], item['y'], item['width'], item['height']))
                    elif ftype == 'Circle':
                        figures.append(Circle(item['x'], item['y'], item['radius']))
                    elif ftype == 'Triangle':
                        figures.append(Triangle(item['x'], item['y'], item['a'], item['b'], item['c']))
            return figures
        except FileNotFoundError:
            print("Файл не найден.")
            return []
