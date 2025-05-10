from shapes import Rectangle, Circle, Triangle
from canvas import Canvas
from storage import Storage

class PaintApp:
    def __init__(self) -> None:
        self._canvas = Canvas()

    def run(self) -> None:
        while True:
            command = input("Enter command (help - список команд): ").strip().lower()
            if command == "exit":
                break
            elif command == "help":
                self._print_help()
            elif command == "add rectangle":
                try:
                    x, y, w, h = map(int, input("Enter x, y, width, height: ").split())
                    rect = Rectangle(x, y, w, h)
                    self._canvas.add_figure(rect)
                    print(f"Rectangle added at index: {len(self._canvas._figures) - 1}")
                except Exception as e:
                    print("Ошибка ввода:", e)
            elif command == "add circle":
                try:
                    x, y, r = map(int, input("Enter x, y, radius: ").split())
                    circle = Circle(x, y, r)
                    self._canvas.add_figure(circle)
                    print(f"Circle added at index: {len(self._canvas._figures) - 1}")
                except Exception as e:
                    print("Ошибка ввода:", e)
            elif command == "add triangle":
                try:
                    x, y, a, b, c = map(int, input("Enter x, y, side a, side b, side c: ").split())
                    triangle = Triangle(x, y, a, b, c)
                    self._canvas.add_figure(triangle)
                    print(f"Triangle added at index: {len(self._canvas._figures) - 1}")
                except Exception as e:
                    print("Ошибка ввода:", e)
            elif command == "fill":
                try:
                    index = int(input("Enter figure index to toggle fill: "))
                    if 0 <= index < len(self._canvas._figures):
                        self._canvas.toggle_fill(index)
                    else:
                        print("Некорректный индекс фигуры.")
                except Exception as e:
                    print("Ошибка ввода:", e)
            elif command == "draw":
                self._canvas.draw()
            elif command == "move":
                try:
                    index = int(input("Enter figure index to move: "))
                    new_x, new_y = map(int, input("Enter new x and y coordinates: ").split())
                    if 0 <= index < len(self._canvas._figures):
                        self._canvas.move_figure(index, new_x, new_y)
                    else:
                        print("Некорректный индекс фигуры.")
                except Exception as e:
                    print("Ошибка ввода:", e)
            elif command == "remove":
                try:
                    index = int(input("Enter figure index to remove: "))
                    self._canvas.remove_figure(index)
                    print(f"Figure at index {index} removed.")
                except Exception as e:
                    print("Ошибка ввода:", e)
            elif command == "save":
                filename = input("Enter filename: ").strip()
                Storage.save(self._canvas, filename)
            elif command == "load":
                filename = input("Enter filename: ").strip()
                figures = Storage.load(filename)
                if figures:
                    self._canvas._figures = figures
            elif command == "undo":
                self._canvas.undo()
            elif command == "redo":
                self._canvas.redo()
            else:
                print("Unknown command.")

    def _print_help(self) -> None:
        print("Commands: add rectangle, add circle, add triangle, fill, draw, move, remove, save, load, undo, redo, exit")

if __name__ == "__main__":
    PaintApp().run()

