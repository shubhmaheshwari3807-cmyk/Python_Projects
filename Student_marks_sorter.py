marks=[]
marks.append(int(input("Enter first student's marks: ")))
marks.append(int(input("Enter second student's marks: ")))
marks.append(int(input("Enter third student's marks: ")))
marks.append(int(input("Enter fourth student's marks: ")))
marks.append(int(input("Enter fifth student's marks: ")))

marks.sort()
print(marks)
print("The maximum marks are", marks[4])
print("The minimum marks are", marks[0])