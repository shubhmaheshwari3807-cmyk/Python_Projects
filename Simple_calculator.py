a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=input("Enter operation: ")

def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def mult(a,b):
    print(a*b)

def div(a,b):
    print(a/b)

if(c=="+"):
    add(a,b)
elif(c=="-"):
    sub(a,b)
elif(c=="*"):
    mult(a,b)
elif(c=="/"):
    div(a,b)
else:
    print("Invalid Operation")