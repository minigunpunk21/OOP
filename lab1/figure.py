from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self):
            pass
    def move(self,new_x,new_y):
        self.x=new_x
        self.y=new_y
