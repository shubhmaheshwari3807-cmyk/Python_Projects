class Student:
    school_name="ABC School"
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks

    def avg(self):
        sum=0
        i=0
        while i<len(self.marks):
            sum+=self.marks[i]
            i+=1
        print("The average is ", sum/3)

student1=Student("Karan", [23,54,20])
student1.avg()
print(Student.school_name)
