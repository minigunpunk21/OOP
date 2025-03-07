from canvas import Canvas
from shapes import Rectangle, Circle, Triangle
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
                    self._canvas.add_figure(Rectangle(x, y, w, h))
                except Exception as e:
                    print("Ошибка ввода:", e)
            elif command == "add circle":
                try:
                    x, y, r = map(int, input("Enter x, y, radius: ").split())
                    self._canvas.add_figure(Circle(x, y, r))
                except Exception as e:
                    print("Ошибка ввода:", e)
            elif command == "add triangle":
                try:
                    x, y, base, height = map(int, input("Enter x, y, base, height: ").split())
                    self._canvas.add_figure(Triangle(x, y, base, height))
                except Exception as e:
                    print("Ошибка ввода:", e)
            elif command == "draw":
                self._canvas.draw()
            elif command == "move":
                try:
                    index, dx, dy = map(int, input("Enter figure index, dx, dy: ").split())
                    self._canvas.move_figure(index, dx, dy)
                except Exception as e:
                    print("Ошибка ввода:", e)
            elif command == "remove":
                try:
                    index = int(input("Enter figure index to remove: "))
                    self._canvas.remove_figure(index)
                except Exception as e:
                    print("Ошибка ввода:", e)
            elif command == "undo":
                self._canvas.undo()
            elif command == "redo":
                self._canvas.redo()
            elif command == "save":
                filename = input("Enter filename: ").strip()
                Storage.save(self._canvas, filename)
            elif command == "load":
                filename = input("Enter filename: ").strip()
                figures = Storage.load(filename)
                if figures:
                    self._canvas._figures = figures
            else:
                print("Unknown command.")

    def _print_help(self) -> None:
        print("Commands:")
        print("  add rectangle - Добавить прямоугольник")
        print("  add circle    - Добавить круг")
        print("  add triangle  - Добавить треугольник")
        print("  move          - Переместить фигуру")
        print("  remove        - Удалить фигуру")
        print("  draw          - Отобразить полотно")
        print("  undo          - Отмена действия")
        print("  redo          - Повтор действия")
        print("  save          - Сохранить полотно")
        print("  load          - Загрузить полотно")
        print("  exit          - Выход")

if __name__ == "__main__":
    PaintApp().run()
