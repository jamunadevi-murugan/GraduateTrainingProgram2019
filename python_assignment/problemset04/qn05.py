class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def eq(self, a, b):
            return (a == self.x and b == self.y)

    def repr(self):
        print('Coordinate(', self.getX(), ',', self.getY(), ')')


cor=Coordinate(11,15)
print(cor.eq(11,15))
print(cor.__str__())
cor.repr()