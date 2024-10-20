import math

class Shape:
    def area(self):
        """Base class method to calculate area"""
        raise NotImplementedError("Subclass must implement area method")

class Rectangle(Shape):
    def __init__(self, length, width):
        """Derived class for rectangles"""
        self.length = length
        self.width = width

    def area(self):
        """Override area method for rectangles"""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """Derived class for circles"""
        self.radius = radius

    def area(self):
        """Override area method for circles"""
        return math.pi * (self.radius ** 2)
