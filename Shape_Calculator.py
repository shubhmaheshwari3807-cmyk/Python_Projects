class MathHelper():
    @staticmethod
    def add(a,b):
        print(a+b)

class Circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=3.14*self.radius*self.radius
        print(area)

MathHelper.add(5,3)
c1=Circle(5)
c1.area()
