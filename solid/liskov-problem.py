class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    def area(self):
        return self._width * self._height


class Square(Rectangle):
    def __init__(self, side):
        super().set_width(side)
        super().set_height(side)

    def set_width(self, width):
        super().set_width(width)
        super().set_height(width)

    def set_height(self, height):
        super().set_height(height)
        super().set_width(height)


def break_liskov(rect, width, height):
    rect.set_width(width)
    rect.set_height(height)
    print(rect.area())


if __name__ == "__main__":
    rect = Rectangle(2, 3)
    square = Square(2)
    break_liskov(square, 3, 4)
