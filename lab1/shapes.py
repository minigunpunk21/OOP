from figure import Figure

class Rectangle(Figure):
    def __init__(self,x,y,width,height):
        super().__init__(x,y)
        self.width = width
        self.height = height
    def draw(self):
        print(f"Drawing triugolnik at({self.x},{self.y} with width {self.width} and height {self.height}")
class Circle(Figure):
    def init(self,x,y,radius):
            super().init(x,y)
            self.radius=radius

