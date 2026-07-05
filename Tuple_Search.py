#Practice question to search for a number in a tuple
x=int(input("Enter a number in the tuple: "))
number=(43, 56, 23, 78, 54, 100)
length=len(number)-1
i=0
while i<=length: 
    y=number[i]
    if(number[i]==x):
        print("The number is present in the tuple at index", number.index(y))
        break
    i+=1
else:
    print("Number not present")
