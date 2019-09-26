class Shape():
    def area(self):
        self.area=0

class Square(Shape):
    def __init__(self, l):
        self.length = l

    def area(self):
        return self.length*self.length

aSquare= Square(3)
print(aSquare.area())