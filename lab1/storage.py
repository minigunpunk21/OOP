import json
from shapes import Rectangle, Circle, Triangle

class Storage:
    @staticmethod
    def save(canvas, filename: str) -> None:
        data = []
        for figure in canvas.figures:
            d = figure.__dict__.copy()
            d['_type'] = figure.__class__.__name__
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
                        figures.append(Rectangle(item['_x'], item['_y'], item['_width'], item['_height']))
                    elif ftype == 'Circle':
                        figures.append(Circle(item['_x'], item['_y'], item['_radius']))
                    elif ftype == 'Triangle':
                        figures.append(Triangle(item['_x'], item['_y'], item['_base'], item['_height']))
            return figures
        except FileNotFoundError:
            print("Файл не найден.")
            return []

