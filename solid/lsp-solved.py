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
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.size = side

    def area(self):
        return self.size**2


def liskov_solved(shape):
    print(shape.area())


if __name__ == "__main__":
    rect = Rectangle(2, 3)
    square = Square(2)
    liskov_solved(rect)
    liskov_solved(square)
