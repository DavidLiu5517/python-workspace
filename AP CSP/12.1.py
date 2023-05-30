class Triangle:
    def __init__(self,side1 = 1.0, side2 = 1.0, side3 = 1.0):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def getPerimeter(self):
        return self.side1 + self.side2 + self.side3
    def getArea(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        a = (p*(p - self.side1)*(p - self.side2)*(p - self.side3)) ** 0.5
        return a
tri1 = Triangle(3,4,5)
print(tri1.getPerimeter(), tri1.getArea())

tri2 = Triangle(2.5,4.3,5.2)
print(tri2.getPerimeter(), tri2.getArea())