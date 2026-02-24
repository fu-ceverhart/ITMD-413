class triangle:
    def __init__(self, base, height, hypotenuse):
        self.base = base
        self.height = height
        self.hypotenuse = hypotenuse

    def area(self):
        return 0.5 * self.base * self.height


    def perimeter(self):
        return self.base + self.height + self.hypotenuse


threepio = triangle(3, 4, 5)
print(threepio.area())
print(threepio.perimeter())
