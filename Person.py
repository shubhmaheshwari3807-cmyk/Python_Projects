class Person():
    def __init__(self, name, age):
        self.name=name
        self.age=age

class Students(Person):
    def __init__(self, name, age, course):
        super().__init__(name,age)
        self.course=course

    def Display(self):
        print(self.name)
        print(self.age)
        print(self.course)

s1=Students("karan", 19, "Hindi")
s1.Display()
