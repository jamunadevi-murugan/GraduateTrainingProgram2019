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

    def __eq__(self, other):
            return self.x == self.y

    def __repr__(self):
        return eval(repr(self.x))==self.x and eval(repr(self.y))==self.y


cor=Coordinate(11,11)
cor1=(cor.x==cor.y)
print(cor1)
print(cor.__str__())
print(cor.__repr__())
