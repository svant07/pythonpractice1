import math

class Figure():

    def __init__(self, *sides, color):
        self.__sides = []
        self.__color = []
        self.sides_count = 0
        self.filled = False
        self.set_color(*color)
        self.set_sides(*sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        for x in (r, g, b):
            if isinstance(x, int) and 1 >= x <= 255:
                return all

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        for side in sides:
            if all(side) > 0 and len(sides) == self.sides_count:
                return True
            else:
                return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    def __init__(self, color, *sides):
        self.color = color
        super().__init__(color, *sides)



    def get_square(self):
        return (self.__radius ** 2) * math.pi

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            super().get_sides(*new_sides)
            self.__radius = new_sides[0] / (2 * math.pi)
        else:
            super().get_sides(1)


class Triangle(Figure):

    def __init__(self, color, *sides, __radius):
        sides_count = 3
        super().__init__(color, *sides)
        self.__radius = __radius

    def get_square(self):
        return math.pi * self.__radius ** 2

class Cube(Figure):
    def __init__(self, color, *sides):
        sides_count = 12
        super().__init__(color, *sides)
        self.__side_len = self.__sides[0]

    #def set_sides(self, *new_sides):
     #   if len(sides)

    #def get_volume(self):
    #    return mul(self.__sides)


circle1 = Circle((200, 200, 100), 10)
#circle1.set_color(55, 66, 77) # Изменится
#print(circle1.get_color())

circle1.set_sides(15) # Изменится
print(circle1.get_sides())

print(len(circle1))






