students=[]
marks=[]
students.append(input("Enter the name of the student: "))
marks.append(int(input("Enter the student's marks: ")))
students.append(input("Enter the name of the student: "))
marks.append(int(input("Enter the student's marks: ")))
students.append(input("Enter the name of the student: "))
marks.append(int(input("Enter the student's marks: ")))
students.append(input("Enter the name of the student: "))
marks.append(int(input("Enter the student's marks: ")))
students.append(input("Enter the name of the student: "))
marks.append(int(input("Enter the student's marks: ")))

marks.sort(reverse=True)
print(marks)
print("The highest marks are", marks[0])
print("The lowest marks are", marks[4])
print("Total number of students are", len(students))

target_marks=int(input("Tell a target marks: "))
count=0
if(marks[0]>target_marks):
    count=count+1
if(marks[1]>target_marks):
    count=count+1
if(marks[2]>target_marks):
    count=count+1
if(marks[3]>target_marks):
    count=count+1
if(marks[4]>target_marks):
    count=count+1
print("The students scoring more than the targetted marks are", count)
