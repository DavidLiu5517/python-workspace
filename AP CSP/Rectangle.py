class Rectangle:
    def __init__(self,width = 1.0, height = 2.0):
        self.width = width
        self.height = height
    def getPerimeter(self):
        return 2 * (self.width + self.height)
    def getArea(self):
        return self.width * self.height
    
rect1 = Rectangle(4, 40)
print(rect1.getPerimeter(), rect1.getArea())

rect2 = Rectangle(3.5, 35.7)
print(rect2.getPerimeter(), rect2.getArea())