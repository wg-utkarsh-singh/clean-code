class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, origin, width, height):
        self.origin = origin
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def print_coordinates(self):
        top_right = self.origin.coordX + self.width
        bottom_left = self.origin.coordY + self.height
        print("Starting Point (X)): " + str(self.origin.coordX))
        print("Starting Point (Y)): " + str(self.origin.coordY))
        print("End Point X-Axis (Top Right): " + str(top_right))
        print("End Point Y-Axis (Bottom Left): " + str(bottom_left))


def build_rectangle():
    rect_origin = Point(50, 100)
    rect = Rectangle(rect_origin, 90, 10)
    return rect


if __name__ == "__main__":
    my_rect = build_rectangle()
    print(my_rect.get_area())
    my_rect.print_coordinates()
