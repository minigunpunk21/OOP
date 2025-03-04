class Canvas:
    def __init__(self):
        self.figures=[]

    def add_figure(self,figure):
        self.figures.append(figure)
    
    def remove_figure(self, index):
        if 0<=index < len(self.figures):
            del self.figures[index]
    
    def move_figure(self,index,new_x,new_y):
        if 0<= index < len(self.figures):
            self.figures[index].move(new_x,new_y)

    def draw_canvas(self):
        for figure in self.figures:
            figure.draw()
