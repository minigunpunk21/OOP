#GOSPODI WORK PLS
from canvas import Canvas
from shapes import Rectangle, Circle

class PaintApp:
    def __init__(self):
        self.canvas = Canvas()
    def run(self):
        while (1):
            command = input("Enter command: ").strip().lower()
            if command == "exit":
                break
            elif command == "add rectangle":
                x,y,w,h = map(int,input("Enter x,y,width,height, pls: ").split())
                self.canvas.add_figure(Rectangle(x,y,w,h))
            elif command == "add circle":
                x, y, r = map(int, input("Enter x, y, radius: ").split())
                self.canvas.add_figure(Circle(x, y, r))
            elif command == "draw":
                self.canvas.draw_canvas()
            else:
                print("IDK whatis")

if __name__ == "__main__":
    PaintApp().run()
