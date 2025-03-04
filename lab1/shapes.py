from figure import Figure

class Rectangle(Figure):
    def init(self,x,y,width,height):
        super().init(x,y)
        self.width = width
        self.height = height
class Circle(Figure):
    def init(self,x,y,radius):
            super().init(x,y)
            self.radius=radius

