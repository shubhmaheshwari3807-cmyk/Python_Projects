record={}
name1=input("Enter the name of first student: ")
m1=int(input("Marks in Physics: "))
m2=int(input("Marks in Chemistry: "))
m3=int(input("Marks in Mathematics: "))
marks_name1=[m1, m2, m3]
avg1=(m1+m2+m3)/3
if(avg1>=90):
    print("A grade")
elif(avg1>=75 and avg1<89):
    print("B grade")
else:
    print("Fail")
name2=input("Enter the name of the second student: ")
n1=int(input("Marks in Physics: "))
n2=int(input("Marks in Chemistry: "))
n3=int(input("Marks in Mathematics: "))
marks_name2=[n1, n2, n3]
avg2=(n1+n2+n3)/3
if(avg2>=90):
    print("A grade")
elif(avg2>=75 and avg2<89):
    print("B grade")
else:
    print("Fail")
record[name1]=f"{avg1:.2f}"
record[name2]=f"{avg2:.2f}"

print(record)