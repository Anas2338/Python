from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width
    

rect1 = Rectangle(10, 5)

print(f"Area of Rectangle: {rect1.area()}")
