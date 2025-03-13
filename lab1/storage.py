import json
from shapes import Rectangle, Circle, Triangle

class Storage:
    @staticmethod
    def save(canvas, filename: str) -> None:
        data = []
        for figure in canvas._figures:
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
                        figures.append(Rectangle(**item))
                    elif ftype == 'Circle':
                        figures.append(Circle(**item))
                    elif ftype == 'Triangle':
                        figures.append(Triangle(**item))
            return figures
        except FileNotFoundError:
            print("Файл не найден.")
            return []
